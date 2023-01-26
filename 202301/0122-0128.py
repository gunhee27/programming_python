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

###############################
# 0126
###############################
# 1932
n = int(input())
arr = [[0] * n for _ in range(n)]
for i in range(n):
    aa = list(map(int, input().split()))
    for j in range(len(aa)):
        arr[i][j] = aa[j]

for i in range(1, n):
    for j in range(n):
        if j == 0:
            arr[i][0] += arr[i - 1][0]
        elif j == n - 1:
            arr[i][j] += arr[i - 1][j - 1]
        else:
            arr[i][j] += max(arr[i - 1][j], arr[i - 1][j - 1])
print(max(arr[n - 1]))

# 2156
n = int(input())
arr = [0] * 10000
for i in range(n):
    arr[i] = int(input())
d = [0] * (10000)
d[0] = arr[0]
d[1] = arr[0] + arr[1]
d[2] = max(arr[0] + arr[2], arr[1] + arr[2], d[1])
for i in range(3, n):
    d[i] = max(d[i - 2] + arr[i], arr[i] + arr[i - 1] + d[i - 3], d[i - 1])
print(max(d))