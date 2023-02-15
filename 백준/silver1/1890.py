n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            continue
        aa = arr[i][j]
        if 0 <= aa + i < n:
            dp[aa + i][j] += dp[i][j]
        if 0 <= aa + j < n:
            dp[i][aa + j] += dp[i][j]

print(dp[n -1][n -1])
