from collections import deque
m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
for _ in range(k):
    sx, sy, fx, fy = map(int, input().split())
    for i in range(sx, fx):
        for j in range(sy, fy):
            arr[j][i] = 1

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
result = []

def bfs(x, y):
    q = deque()
    q.append((x, y))
    count = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and arr[ny][nx] == 0:
                arr[ny][nx] = 1
                q.append((nx, ny))
                count += 1
    return count


for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = 1
            result.append(bfs(j, i))
print(len(result))
result.sort()
for i in result:
    print(i, end=" ")