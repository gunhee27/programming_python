import sys
sys.setrecursionlimit(10000)
n = int(input())
arr = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0] * (n + 1)
def dfs(start):
    for i in arr[start]:
        if visited[i] == 0:
            visited[i] = start
            dfs(i)
dfs(1)
for i in range(2, n + 1):
    print(visited[i])
