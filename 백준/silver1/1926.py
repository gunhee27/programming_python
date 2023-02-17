from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                q.append([nx, ny])
                arr[nx][ny] += arr[x][y]
                count += 1
    if count == 0: return count + 1
    else: return count

result = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            result.append(bfs(i, j))

print(len(result))
if len(result) == 0:
    print(0)
else:
    print(max(result))