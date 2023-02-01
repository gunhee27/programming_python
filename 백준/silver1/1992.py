n = int(input())
arr = []
for i in range(n):
    arr.append(list(input().strip()))
def tree(x, y, n):
    real = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if real != arr[i][j]:
                print('(', end='')
                tree(x, y, n // 2)
                tree(x, y + n // 2, n // 2)
                tree(x + n // 2, y, n // 2)
                tree(x + n // 2, y + n // 2, n // 2)
                print(')', end='')
                return
    if real == '0':
        print("0", end='')
        return
    else:
        print("1", end='')
        return

tree(0, 0, n)