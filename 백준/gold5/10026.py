from collections import deque

n = int(input())
arr = []
for i in range(n):
    arr.append(list(input().rstrip()))

q = deque()
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    q.append([x, y])
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])


visited = [[0] * n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count += 1

visited = [[0] * n for _ in range(n)]
count1 = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count1 += 1

print(count, count1)