from collections import deque
f, s, g, u, d = map(int, input().split())
visited = [-1 for _ in range(f + 1)]

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        aa = q.popleft()
        if aa == g:
            return visited[aa]
        for i in (aa - d, aa + u):
            if 1 <= i <= f and visited[i] == -1:
                q.append(i)
                visited[i] = visited[aa] + 1
    return "use the stairs"

print(bfs(s))