###############################
# 0129
###############################
# 14888
n = int(input())
arr = list(map(int, input().split()))

a, b, c, d = map(int, input().split())
maxi = -1e9
mini = 1e9

def dfs(d, total, add, minus, multi, div):
    global maxi, mini
    if d == n:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return

    if add:
        dfs(d + 1, total + arr[d], add - 1, minus, multi, div)
    if minus:
        dfs(d + 1, total - arr[d], add, minus - 1, multi, div)
    if multi:
        dfs(d + 1, total * arr[d], add, minus, multi - 1, div)
    if div:
        dfs(d + 1, int(int(total) / arr[d]), add, minus, multi, div - 1)


dfs(1, arr[0], a, b, c, d)
print(maxi)
print(mini)

#1991
n = int(input())
tree = {}
for i in range(n):
    root, left, right= input().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

###############################
# 0130
###############################
# 1141
n = int(input())
arr = []
for i in range(n):
    arr.append(input())
count = 0
arr.sort(key=len)
for i in range(n):
    flag = False
    for j in range(i + 1, n):
        if arr[i] == arr[j][0:len(arr[i])]:
            flag = True
            break
    if not flag:
        count += 1
print(count)


# 11052
n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for k in range(1, i + 1):
        dp[i] = max(dp[i - k] + arr[k], dp[i])
print(dp[n])

# 18870
n = int(input())
arr = list(map(int, input().split()))
num = sorted(set(arr))
new_arr = {}
for i in range(len(num)):
    new_arr[num[i]] = i
for i in range(n):
    print(new_arr[arr[i]], end=' ')

###############################
# 0131
###############################
# 1138
n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n
for p in range(1, n + 1):
    t = arr[p - 1]
    cnt = 0
    for i in range(n):
        if cnt == t and ans[i] == 0:
            ans[i] = p
            break
        elif ans[i] == 0:
            cnt += 1
for i in ans:
    print(i, end=" ")

# 2468
from collections import deque
n = int(input())
arr = []
maxi = 0
for i in range(n):
    temp = list(map(int, input().split()))
    maxi = max(maxi, max(temp))
    arr.append(temp)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, h):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0 <= nx < n and 0 <= ny < n and arr[nx][ny] > h and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))


result = []
for i in range(maxi):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if arr[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                cnt += 1
    result.append(cnt)

print(max(result))




