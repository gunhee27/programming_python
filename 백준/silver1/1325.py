from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

def bfs(start):
    q = deque()
    q.append(start)
    visited = [0] * (n + 1)
    visited[start] = 1
    count = 1
    while q:
        aa = q.popleft()
        for i in arr[aa]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                count += 1
    return count

maxi = 0
result = []
for i in range(1, n + 1):
    count = bfs(i)
    if count > maxi:
        maxi = count
        result.clear()
        result.append(i)
    elif count == maxi:
        result.append(i)

print(*result)