n, k = map(int, input().split())
arr = [[1 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n + 1:
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

if n == 1:
    print(1)
else:
    print(arr[n - k][k] % 10007)