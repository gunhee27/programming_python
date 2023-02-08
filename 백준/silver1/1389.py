from collections import deque
n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for i in range(m):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        aa = q.popleft()
        for i in arr[aa]:
            if not visited[i]:
                visited[i] = visited[aa] + 1
                q.append(i)

result = []
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    bfs(i)
    result.append(sum(visited))
print(result.index(min(result)) + 1)