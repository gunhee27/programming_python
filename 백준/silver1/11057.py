n = int(input())
arr = [1] * 10
for _ in range(n - 1):
    for i in range(1, 10):
       arr[i] += arr[i - 1]
print(sum(arr) % 10007)
