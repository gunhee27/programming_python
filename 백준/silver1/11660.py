import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] + arr[i - 1][j - 1] - dp[i - 1][j - 1]
for _ in range(m):
    sx, sy, fx, fy = map(int, input().split())
    sum = dp[fx][fy] - dp[sx - 1][fy] - dp[fx][sy - 1] + dp[sx - 1][sy - 1]
    print(sum)