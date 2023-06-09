from collections import deque
r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(input().rstrip()))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(a, b):
    sheep = 0
    wolf = 0
    q = deque()
    q.append((a, b))
    if arr[a][b] == 'o':
        sheep += 1
    elif arr[a][b] == 'v':
        wolf += 1
    arr[a][b] = '#'
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != '#':
                if arr[nx][ny] == 'o':
                    sheep += 1
                elif arr[nx][ny] == 'v':
                    wolf += 1
                arr[nx][ny] = '#'
                q.append((nx, ny))
    if sheep > wolf:
        return sheep, 0
    else:
        return 0, wolf

resultS = 0
resultW = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] != '#':
            s, w = bfs(i, j)
            resultS += s
            resultW += w

print(resultS, resultW)






