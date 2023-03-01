n, m, k = map(int, input().split())

def find(x, y):
    dp = [[0] * (y + 1) for _ in range(x + 1)]
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[x][y]

if k == 0:
    print(find(n, m))
else:
    sx = (k - 1) // m + 1
    sy = k - (sx - 1) * m
    first = find(sx, sy)
    second = find(n - sx + 1, m - sy + 1)
    print(first * second)
