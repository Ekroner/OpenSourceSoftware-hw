import requests

# GitHub API 端点
url = 'https://api.github.com/repos/django/djangoproject.com/issues'
#url = 'https://api.github.com/repos/django/channels/issues'
params = {'labels': 'bug'}  # 只获取带有 bug 标签的 issue

# 发起请求
response = requests.get(url, params=params)

# 检查请求是否成功
if response.status_code == 200:
    issues = response.json()
    bug_count = len(issues)  # 统计 bug 的数量
    print(f'Bug 数量：{bug_count}')
else:
    print('请求失败', response.status_code)