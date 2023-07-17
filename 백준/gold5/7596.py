from collections import deque
m, n, h = map(int, input().split())
arr = []
q = deque([])
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
    arr.append(temp)

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and arr[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                q.append([nx, ny, nz])
                visited[nx][ny][nz] = True
                arr[nx][ny][nz] = arr[x][y][z] + 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1 and not visited[i][j][k]:
                q.append([i, j, k])
                visited[i][j][k] = True

bfs()

answer = 0

for a in arr:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(b))

print(answer-1)
