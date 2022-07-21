n = int(input())
arr = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid + 1
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


arr.sort()

for i in x:
    result = binary_search(arr, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start + end)// 2
    for x in arr:
        if x > mid:
            a = x - mid
            total += a
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
