import requests
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
from collections import defaultdict, Counter
from datetime import datetime, timedelta
from jinja2 import Template
import pdfkit

# ==================== 配置部分 ====================
GITHUB_TOKEN = "YOUR_TOKEN"  # 替换为你的GitHub Token
REPO_OWNER = "django"
REPO_NAME = "django"
OUTPUT_DIR = "analysis_reports"
# =================================================

# 配置请求头
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits"

def fetch_commit_history(start_date, end_date):
    """从GitHub获取提交历史"""
    commits = []
    page = 1
    while True:
        try:
            params = {
                "per_page": 100,
                "page": page,
                "since": start_date,
                "until": end_date
            }
            response = requests.get(URL, headers=HEADERS, params=params)
            response.raise_for_status()  # 触发HTTPError异常
            
            data = response.json()
            if not data:
                break
            commits.extend(data)
            page += 1
            
            # GitHub API限制检测（示例处理）
            if 'X-RateLimit-Remaining' in response.headers:
                remaining = int(response.headers['X-RateLimit-Remaining'])
                if remaining < 10:
                    print(f"Warning: API rate limit remaining: {remaining}")
                    
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {str(e)}")
            break
            
    return commits

def analyze_commit_data(commits):
    """执行完整数据分析"""
    # 提交频率分析
    daily_commits = defaultdict(int)
    # 贡献者分析
    contributors = []
    # 时间分布分析
    weekday_commits = 0
    weekend_commits = 0
    
    for commit in commits:
        try:
            # 提交日期处理
            date_str = commit['commit']['author']['date'][:10]
            date = datetime.strptime(date_str, "%Y-%m-%d")
            
            # 提交频率统计
            daily_commits[date_str] += 1
            
            # 贡献者统计
            contributors.append(commit['commit']['author']['name'])
            
            # 时间分布统计
            if date.weekday() >= 5:
                weekend_commits += 1
            else:
                weekday_commits += 1
                
        except KeyError as e:
            print(f"Warning: Missing key in commit data: {str(e)}")
            continue
            
    return {
        "daily_commits": daily_commits,
        "contributor_activity": Counter(contributors),
        "weekday_commits": weekday_commits,
        "weekend_commits": weekend_commits
    }

def visualize_data(results, output_dir):
    """生成可视化图表并保存"""
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 提交频率折线图
    dates = list(results['daily_commits'].keys())
    counts = list(results['daily_commits'].values())
    
    plt.figure(figsize=(14, 7))
    plt.plot(dates, counts, marker='o', linestyle='-', color='#2c7fb8')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Commits', fontsize=12)
    plt.title(f'Commit Frequency ({dates[0]} to {dates[-1]})', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'commit_frequency.png'), dpi=300)
    plt.close()
    
    # 贡献者活跃度柱状图（Top 15）
    contributors = list(results['contributor_activity'].keys())[:15]
    commits = list(results['contributor_activity'].values())[:15]
    
    plt.figure(figsize=(14, 7))
    bars = plt.bar(contributors, commits, color='#fdae6b')
    plt.xlabel('Contributors', fontsize=12)
    plt.ylabel('Commits', fontsize=12)
    plt.title('Top 15 Contributors', fontsize=14)
    plt.xticks(rotation=75, fontsize=8)
    
    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}', ha='center', va='bottom', fontsize=8)
                
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'contributor_activity.png'), dpi=300)
    plt.close()

def generate_report(results, start_date, end_date, output_dir):
    """生成分析报告"""
     # 获取图片绝对路径
    commit_freq_img = os.path.abspath(os.path.join(output_dir, 'commit_frequency.png')).replace('\\', '/')
    contributor_img = os.path.abspath(os.path.join(output_dir, 'contributor_activity.png')).replace('\\', '/')
    # HTML模板
    template = Template('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Commit Analysis Report</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #2c7fb8; border-bottom: 2px solid #eee; }
            .metrics { background: #f9f9f9; padding: 20px; border-radius: 5px; }
            img { max-width: 100%; margin: 20px 0; border: 1px solid #ddd; }
        </style>
    </head>
    <body>
        <h1>Code Commit Analysis Report</h1>
        <div class="metrics">
            <p>Analysis Period: {{ start_date }} to {{ end_date }}</p>
            <p>Total Commits: {{ total_commits }}</p>
            <p>Weekday Commits: {{ weekday }} ({{ weekday_ratio }}%)</p>
            <p>Weekend Commits: {{ weekend }} ({{ weekend_ratio }}%)</p>
        </div>
        
        <h2>Commit Frequency</h2>
        <img src="{{ commit_frequency_img }}">
        
        <h2>Contributor Activity</h2>
        <img src="{{ contributor_activity_img }}">
    </body>
    </html>
    ''')
    
    # 计算比例
    total = results['weekday_commits'] + results['weekend_commits']
    weekday_ratio = round(results['weekday_commits']/total*100, 1)
    weekend_ratio = round(results['weekend_commits']/total*100, 1)
    
    # 渲染模板
    html_content = template.render(
        start_date=start_date,
        end_date=end_date,
        total_commits=sum(results['daily_commits'].values()),
        weekday=results['weekday_commits'],
        weekend=results['weekend_commits'],
        weekday_ratio=weekday_ratio,
        weekend_ratio=weekend_ratio,
        commit_frequency_img=f'file:///{commit_freq_img}',
        contributor_activity_img=f'file:///{contributor_img}'
    )
    
    # 保存报告
    report_path = os.path.join(output_dir, 'report.html')
    with open(report_path, 'w') as f:
        f.write(html_content)
        
    # 生成PDF版本
    try:
        options = {
            'disable-javascript': None,
            'enable-local-file-access': None
        }
        config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        pdfkit.from_file(report_path, os.path.join(output_dir, 'report.pdf'), configuration=config, options=options)
    except Exception as e:
        print(f"PDF generation failed: {str(e)}")

def export_data(results, output_dir):
    """导出结构化数据"""
    # 提交频率数据
    pd.DataFrame({
        'date': results['daily_commits'].keys(),
        'commits': results['daily_commits'].values()
    }).to_csv(os.path.join(output_dir, 'daily_commits.csv'), index=False)
    
    # 贡献者数据
    with open(os.path.join(output_dir, 'contributors.json'), 'w') as f:
        json.dump(results['contributor_activity'], f)

def main(days=180):
    """主控制流程"""
    # 设置时间范围
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    
    # 创建带时间戳的输出目录
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_dir = os.path.join(OUTPUT_DIR, f"report_{timestamp}")
    
    print("="*50)
    print(f"Starting analysis for {REPO_OWNER}/{REPO_NAME}")
    print(f"Time range: {start_date} to {end_date}")
    print("="*50)
    
    try:
        # 数据采集
        print("\n[1/4] Fetching commit history...")
        commits = fetch_commit_history(start_date, end_date)
        print(f"Fetched {len(commits)} commits")
        
        # 数据分析
        print("\n[2/4] Analyzing data...")
        results = analyze_commit_data(commits)
        
        # 数据可视化
        print("\n[3/4] Generating visualizations...")
        visualize_data(results, output_dir)
        
        # 生成报告
        print("\n[4/4] Generating report...")
        generate_report(results, start_date, end_date, output_dir)
        export_data(results, output_dir)
        
        print("\nAnalysis completed successfully!")
        print(f"Report saved to: {os.path.abspath(output_dir)}")
        
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        raise

if __name__ == "__main__":
    # 示例：分析最近365天的数据
    main(days=365)
