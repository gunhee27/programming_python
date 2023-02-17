n = int(input())
str_input = list(input().split())
visited = [0] * 10
maxi, mini = "", ""
def check(i, j, c):
    if c == "<":
        return i < j
    else:
        return i > j

def dfs(depth, s):
    global maxi, mini
    if depth == n + 1:
        if len(mini) == 0:
            mini = s
        else:
            maxi = s
        return
    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1], str(i), str_input[depth - 1]):
                visited[i] = 1
                dfs(depth + 1, s + str(i))
                visited[i] = 0

dfs(0, "")
print(maxi)
print(mini)