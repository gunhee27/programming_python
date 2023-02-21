n, m = map(int, input().split())
arrA = [list(map(int, input().rstrip())) for _ in range(n)]
arrB = [list(map(int, input().rstrip())) for _ in range(n)]

def reverse(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if arrA[i][j] == 0:
                arrA[i][j] = 1
            else:
                arrA[i][j] = 0

def check():
    for i in range(n):
        for j in range(m):
            if arrA[i][j] != arrB[i][j]:
                return False
    return True

count = 0
for i in range(n - 2):
    for j in range(m - 2):
        if arrA[i][j] != arrB[i][j]:
            reverse(i, j)
            count += 1

if check():
    print(count)
else:
    print(-1)