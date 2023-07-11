n, k = map(int, input().split())
arr = [[0, 0]]
value = [[0 for _ in range(k + 1)] for i in range(n + 1)]
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = arr[i][0]
        v = arr[i][1]
        if j < w:
            value[i][j] = value[i - 1][j]
        else:
            value[i][j] = max(value[i - 1][j], value[i - 1][j - w] + v)

print(value[n][k])

