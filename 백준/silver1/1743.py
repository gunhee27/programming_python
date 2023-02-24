from collections import deque
n, m, k = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1

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
                arr[nx][ny] = 2
                count += 1
    return count

result = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            result.append(bfs(i, j))

print(max(result))