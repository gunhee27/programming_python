n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
minus = 0
plus = 0
zero = 0

def dfs(x, y, n):
    global minus, plus, zero
    p = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != p:
                for k in range(3):
                    for j in range(3):
                        dfs(x + k * n // 3, y + j * n // 3, n // 3)
                return
    if p == -1:
        minus += 1
    elif p == 0:
        zero += 1
    else:
        plus += 1

dfs(0,0,n)
print(f'{minus}\n{zero}\n{plus}')
