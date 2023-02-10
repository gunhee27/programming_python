import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append([a, b])
    arr.sort()
    count = 1
    maxi = arr[0][1]
    for i in range(1, n):
        if maxi > arr[i][1]:
            count += 1
            maxi = arr[i][1]
    print(count)