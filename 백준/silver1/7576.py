from collections import deque
def dfs():
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if x == fx and y == fy:
            print(visited[fx][fy] - 1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


T = int(input())
for _ in range(T):
    n = int(input())
    visited = [[0] * n for _ in range(n)]
    sx, sy = map(int, input().split())
    fx, fy = map(int, input().split())
    dx = [-2, -2, -1, 1, 2, 2, 1, -1]
    dy = [-1, 1, 2, 2, 1, -1, -2, -2]
    dfs()

