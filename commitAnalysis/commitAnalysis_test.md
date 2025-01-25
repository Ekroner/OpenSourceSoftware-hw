
# Django 项目提交历史分析工具说明

## 概述
本工具用于分析 Django 项目的提交历史，包括提交频率、贡献者活跃度和提交时间分布。通过调用 GitHub API 获取提交数据，并使用 Python 进行数据分析和可视化。

## 功能
获取提交历史：从 GitHub 获取指定时间范围内的提交记录。

分析提交频率：统计每天的提交数量。

分析贡献者活跃度：统计每个贡献者的提交数量。

分析提交时间分布：统计工作日和周末的提交数量。

可视化提交频率：绘制每日提交数量的折线图。

可视化贡献者活跃度：绘制每个贡献者提交数量的柱状图。步探讨模型的优化与改进方向。

## 代码结构
```
fetch_commit_history(start_date, end_date) #获取指定时间范围内的提交历史。

analyze_commit_frequency(commits) #分析提交频率。

analyze_contributor_activity(commits) #分析贡献者活跃度。

analyze_commit_time_distribution(commits) #分析提交时间分布。

plot_commit_frequency(daily_commits) #可视化提交频率。

plot_contributor_activity(contributor_activity) #可视化贡献者活跃度。

main() #主函数，执行整个分析流程。

```

## 运行结果
### 控制台输出
```
Total commits fetched: 457
Analysis period: 2024-07-17 to 2025-01-13
Daily commits analysis completed.
Contributor activity analysis completed.
Weekday commits: 376, Weekend commits: 81
```

### 可视化图表
设定时间为2025-1-13到2024-10-15
![](https://github.com/Ekroner/OpenSourceSoftware-hw/blob/09132e27375fe41b4e26657aa647ecd17faf1df2/commitAnalysis/commit_frequency.png)
![](https://github.com/Ekroner/OpenSourceSoftware-hw/blob/09132e27375fe41b4e26657aa647ecd17faf1df2/commitAnalysis/contributor_activity.png)
