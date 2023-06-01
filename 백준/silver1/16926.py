n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

start = min(n, m) // 2
for _ in range(r):
    for i in range(start):
        x, y = i, i
        temp = arr[x][y]
        for l in range(i + 1, n - i):
            x = l
            prev = arr[x][y]
            arr[x][y] = temp
            temp = prev
        for d in range(i + 1, m - i):
            y = d
            prev = arr[x][y]
            arr[x][y] = temp
            temp = prev
        for rr in range(i + 1, n - i):
            x = n - rr - 1
            prev = arr[x][y]
            arr[x][y] = temp
            temp = prev
        for u in range(i + 1, m - i):
            y = m - u - 1
            prev = arr[x][y]
            arr[x][y] = temp
            temp = prev

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
