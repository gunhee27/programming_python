from collections import deque
m, n = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque([])
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx, ny])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j])
bfs()
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit(0)
    result = max(result, max(arr[i]))
print(result - 1)

