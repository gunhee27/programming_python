import sys
arr = [True for _ in range(1000001)]
for i in range(2, 1001):
    if arr[i]:
        for j in range(i + i, 1000001, i):
            arr[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0: break
    for i in range(3, len(arr)):
        if arr[i] and arr[n - i]:
            print(n, "=", i, "+", n - i )
            break
    else:
        print("Goldbach's conjecture is wrong.")