n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
zero = 0
one = 0

def sol(x, y, n):
    global zero, one
    aa = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y + n):
            if aa != arr[i][j]:
                sol(x, y, n//2)
                sol(x, y + n // 2,  n//2)
                sol(x + n // 2, y, n//2)
                sol(x + n //2, y + n //2, n//2)
                return
    if aa == 0:
        zero += 1
    else:
        one += 1

sol(0, 0, n)
print(zero)
print(one)