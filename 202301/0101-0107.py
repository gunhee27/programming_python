###############################
# 0101
###############################
# 1182
from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(1, n + 1):
    temp = list(combinations(arr, i))
    for j in temp:
        if sum(j) == s:
            count += 1
print(count)

# 1198
from itertools import combinations
n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

temp = list(combinations(arr, 3))
maxTri = 0
for i in temp:
    x = i[0][0] * i[1][1] + i[1][0] * i[2][1] + i[2][0] * i[0][1]
    y = i[1][0] * i[0][1] + i[2][0] * i[1][1] +i[0][0] * i[2][1]
    result = abs(x - y) * 0.5
    if result > maxTri:
        maxTri = result
print(maxTri)

###############################
# 0102
###############################
# 1254
def dual(s):
    for i in range(len(s)):
        if s[i] == s[len(s) - i - 1]:
            continue
        else:
            return 0
    return 1

s = input()
if dual(s) == 1:
    print(len(s))
else:
    for i in range(len(s)):
       temp = s + s[:i][::-1]
       if dual(temp) == 1:
           print(len(temp))
           break


###############################
# 0103
###############################
# 1206 ============실패============
import math

def gcd_two(a,b):
    while b!=0:
        a, b = b, a % b
    return a

n = int(input())
arr = []
for i in range(n):
    arr.append(float(input()))
result = []

for i in arr:
    num = 0
    maxi = i * 1000
    while num < maxi:
        num += 1
        if num * i == int(num * i):
            maxi = num
        elif (math.floor((math.ceil(num * i) / num) * 1000)) / 1000 == i:
            maxi = num
    if num == 0:
        result.append(1)
    else: result.append(num)
gcdArr = result[0]
lcmArr = result[0]
for i in range(len(result)):
    grdArr = gcd_two(lcmArr, result[i])
    lcmArr = (lcmArr * result[i]) // grdArr
print(lcmArr)

# 9095
t = int(input())
dp = [0] * 12
dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 4
for i in range(t):
    a = int(input())
    if a >= 4:
        for j in range(4, a + 1):
            dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3]
    print(dp[a])

###############################
# 0104
###############################
# 1260
from collections import deque

n, m, v = map(int, input().split())
visited = [0] * (n + 1)
visitedBfs = [0] * (n + 1)
arr = [[0] * (n + 1) for j in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1


def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        if visited[i] == 0 and arr[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visitedBfs[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if visitedBfs[i] == 0 and arr[v][i] == 1:
                queue.append(i)
                visitedBfs[i] = 1

dfs(v)
print()
bfs(v)

# 1912
n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
    arr[i] = max(arr[i], arr[i - 1] + arr[i])
print(max(arr))

###############################
# 0105
###############################
# 11053
n = int(input())
arr = list(map(int,input().split()))
dp = [0] * n
for i in range(n):
    maxi = arr[i]
    count = 1
    for j in range(n):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))

# 11724
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

def dfs(v):
    visited[v] = True
    for k in range(1, n + 1):
        if not visited[k] and arr[v][k] == 1:
            dfs(k)

for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = arr[y][x] = 1

for g in range(1, n + 1):
    if not visited[g]:
        dfs(g)
        count += 1
print(count)