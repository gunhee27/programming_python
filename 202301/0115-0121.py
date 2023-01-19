###############################
# 0116
###############################
# 1874
n = int(input())
arr = []
answer = []
cur = 1
flag = 0
for i in range(n):
    a = int(input())
    while cur <= a:
        arr.append(cur)
        answer.append("+")
        cur += 1
    if arr[-1] == a:
        arr.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    for i in answer:
        print(i)

###############################
# 0117
###############################
# 10799
n = input()
stack = []
count = 0
for i in range(len(n)):
    if n[i] == '(':
        stack.append('(');
    else:
        stack.pop()
        if n[i - 1] == '(':
            count += len(stack)
        else:
            count += 1
print(count)

# 6603
from itertools import combinations
while 1:
    n = list(map(int, input().split()))
    if n[0] == 0: break
    k = n[0]
    arr = n[1:]
    result = list(combinations(arr, 6))
    for i in result:
        for j in i:
            print(j, end=' ')
        print()
    print()

###############################
# 0119
###############################
# 2178
from collections import deque

n, m = map(int, input().split())
arr = [[] * m for _ in range(n)]
for i in range(n):
    temp = input()
    for j in temp:
        arr[i].append(int(j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx, ny])
    return arr[n - 1][m - 1]

print(bfs(0, 0))
