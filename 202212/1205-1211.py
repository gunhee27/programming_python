# 수열정렬
n = int(input())
arr = list(map(int, input().split()))
visited = [0] * n;
list = sorted(arr)
for i in range(n):
    x = list.index(arr[i])
    print(x + visited[x], end=" ")
    visited[x] += 1

#회전하는 큐
from collections import deque
N, M = map(int, input().split())
queue = deque()
arr = deque(list(map(int, input().split())))
for i in range(N):
    queue.append(i + 1)
count = 0
while len(arr) > 0:
    x = arr.popleft()
    qLen = len(queue)
    i = queue.index(x)
    if i < qLen - i:
        k = 0
        while k < i:
            a = queue.popleft()
            queue.append(a)
            k += 1
            count += 1
    else:
        k = 0
        while k < qLen - i:
            a = queue.pop()
            queue.appendleft(a)
            k += 1
            count += 1
    if queue[0] == x:
        a = queue.popleft()
print(count)

#2338
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)

#1026
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort()
count = 0
for i in range(N):
    count += A[i] * B[i]
print(count)

#1003
T = int(input())
for i in range(T):
    N = int(input())
    a, b = 0, 1
    for j in range(2, N + 1):
        result = a + b
        a = b
        b = result
    if N == 0:
        print(b, a)
    else: print(a, b)

#1004
T = int(input())
for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    for j in range(n):
        a, b, r = map(int, input().split())
        if ((x1 - a) * (x1 - a) + (y1 - b) *(y1 -b) > r * r) ^ ((x2 - a) * (x2 - a) + (y2 - b) *(y2 -b) > r * r):
            count += 1
    print(count)

#1057
n, a, b = map(int, input().split())
count = 0
while a != b:
    a -= a // 2
    b -= b // 2
    count += 1
print(count)

#1063
k, r, n = input().split()
kx, ky = ord(k[0]) - 64, int(k[1])
rx, ry = ord(r[0]) - 64, int(r[1])
n = int(n)
arr = ["R", "L", "B", "T", "RT", "LT", "RB", "LB"]
x = [1, -1, 0, 0, 1, -1, 1, -1]
y = [0, 0, -1, 1, 1, 1, -1, -1]
for i in range(n):
    move = input()
    pos = arr.index(move)
    nx, ny = kx + x[pos], ky + y[pos]
    if nx <= 0 or nx > 8 or ny <= 0 or ny > 8:
        continue
    elif nx == rx and ny == ry:
        nrx, nry = rx + x[pos], ry + y[pos]
        if nrx <= 0 or nrx > 8 or nry <= 0 or nry > 8 or nx <= 0 or nx > 8 or ny <= 0 or ny > 8:
            continue
        else:
            rx, ry = nrx, nry
            kx, ky = nx, ny
    else:
        kx, ky = nx, ny
print(chr(kx + 64) + str(ky))
print(chr(rx + 64) + str(ry))

#1072
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
percent = y * 100 // x
if percent >= 99:
    print(-1)
else:
    left = 1
    right = x
    count = 0
    while left <= right:
        mid = (left + right) // 2
        if percent < ((y + mid) * 100 // x + mid):
            right = mid - 1
            count = mid
        else:
            left = mid + 1
print(count)

#1920
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
temp = list(map(int, input().split()))

for i in temp:
    left = 0
    right = N - 1
    isExist = False

    while left <= right:
        mid = (left + right) // 2
        if i == arr[mid]:
            isExist = True
            print(1)
            break
        else:
            if i > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
    if not isExist:
        print(0)

#2512
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
left = 0
right = max(arr)
while left <= right:
    mid = (left + right) // 2
    count = 0
    for i in arr:
        if i >= mid:
            count += mid
        else:
            count += i
    if count <= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)

#1463
N = int(input())
dp = [0] * (N + 1)
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
print(dp[N])

#1012
import sys
sys.setrecursionlimit(10000)
def dfs(x, y, n, m, arr):
    if 0 <= x < n and 0 <= y < m:
        if arr[x][y] == 1:
            arr[x][y] = 0
            dfs(x - 1, y, n, m, arr)
            dfs(x + 1, y, n, m, arr)
            dfs(x, y - 1, n, m ,arr)
            dfs(x, y + 1, n, m ,arr)
            return True
    return False

T = int(input())
for _ in range(T):
    result = 0
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1
    for i in range(n):
        for j in range(m):
            if dfs(i, j, n, m, arr) == True:
                result += 1

    print(result)

#1166
# ========잘못된 풀이========
import math

n, l, w, h = map(int, input().split())
left = 0
right = math.gcd(l, w, h)
for _ in range(10000):
    mid = (left + right) / 2
    if (l // mid) * (w // mid) * (h / mid) >= n:
        left = mid
    else:
        right = mid
print("%.10f" %(right))

# ========옳은 풀이========
import sys

n, l, w, h = map(int, sys.stdin.readline().split())
left = 0
right = max(l, w, h)
for _ in range(10000):
    mid = (left + right) / 2
    if (l // mid) * (w // mid) * (h // mid) >= n:
        left = mid
    else:
        right = mid
print("%.10f" %(right))