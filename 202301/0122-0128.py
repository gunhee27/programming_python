###############################
# 0122
###############################
# 1931
n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])
arr.sort(key = lambda x: (x[1], x[0]))
cnt = 1
end = arr[0][1]
for i in range(1, n):
    if arr[i][0] >= end:
        cnt += 1
        end = arr[i][1]
print(cnt)

###############################
# 0125
###############################
# 1697
from collections import deque
n, k = map(int, input().split())
visited = [0] * 100001

def bfs():
    q = deque()
    q.append(n)
    while q:
        a = q.popleft()
        if a == k:
            print(visited[a])
            break
        for i in (a - 1, a + 1, 2 * a):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[a] + 1
                q.append(i)

bfs()
