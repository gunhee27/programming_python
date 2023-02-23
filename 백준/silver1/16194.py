n = int(input())
arr = [0] + list(map(int, input().split()))
for i in range(n + 1):
    for j in range(1, i + 1):
        arr[i] = min(arr[j] + arr[i - j], arr[i])

print(arr[n])