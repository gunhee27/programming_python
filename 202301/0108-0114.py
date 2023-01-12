###############################
# 0109
###############################
# 2805
import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left, right = 1, max(arr)
while left <= right:
    mid = (left + right) // 2
    s = 0
    for i in arr:
        if i >= mid:
            s = s + (i - mid)
    if s < m:
        right = mid - 1
    else:
        left = mid + 1
print(right)

###############################
# 0110
###############################
# 1541
arr = input().split('-')
result = []
for i in arr:
    if i.find('+') >= 0:
        num = 0
        temp = i.split('+')
        for j in temp:
            num += int(j)
        result.append(num)
    else:
        result.append(int(i))
print(result[0] - sum(result[1:]))

# 1654
k, n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))

left = 1
right = max(arr)
while left <= right:
    mid = (left + right) // 2
    s = 0
    for i in arr:
        s += (i // mid)
    if s >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)

###############################
# 0111
###############################
# 14889
n = int(input())
arr = []
for t in range(n):
    arr.append(list(map(int, input().split())))
visited = [False] * (n + 1)
min_diff = 1e9


def dfs(depth, index):
    global min_diff
    if depth == (n // 2):
        start = 0
        link = 0
        for i in range(n):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                    start += arr[j][i]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
                    link += arr[j][i]
        min_diff = min(min_diff, abs(start - link))

    for k in range(index, n):
        if not visited[k]:
            visited[k] = True
            dfs(depth + 1, k + 1)
            visited[k] = False


dfs(0, 0)
print(min_diff)

# 1972
import heapq
import sys

n = int(input())
q = []
for _ in range(n):
    a = int(sys.stdin.readline())
    if a > 0:
        heapq.heappush(q, a)
    elif a == 0:
        if q:
            min_num = heapq.heappop(q)
            print(min_num)
        else:
            print(0)

# 11279
import heapq
import sys

n = int(input())
q = []
for _ in range(n):
    a = int(sys.stdin.readline())
    if a > 0:
        heapq.heappush(q, a * (-1))
    elif a == 0:
        if q:
            max_num = heapq.heappop(q)
            print(max_num * (-1))
        else:
            print(0)


###############################
# 0112
###############################
# 4963
import sys
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def dfs(x, y):
    visited[x][y] = 1
    if arr[x][y] == 1:
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    dfs(nx, ny)

while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        arr.append(list(map(int, input().split())))
    answer = 0
    for a in range(h):
        for b in range(w):
            if arr[a][b] == 1 and not visited[a][b]:
                dfs(a, b)
                answer += 1
            else: continue

    print(answer)
#######################################################
from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def bfs(x, y):
    visited[x][y] = 1
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(8):
            na = x + dx[i]
            nb = y + dy[i]
            if 0 <= na < h and 0 <= nb < w:
                if arr[na][nb] == 1 and not visited[na][nb]:
                    visited[na][nb] = 1
                    q.append((na, nb))

while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        arr.append(list(map(int, input().split())))
    answer = 0
    for a in range(h):
        for b in range(w):
            if arr[a][b] == 1 and not visited[a][b]:
                bfs(a, b)
                answer += 1
    print(answer)
