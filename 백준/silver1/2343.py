n, m = map(int, input().split())
arr = list(map(int, input().split()))
left = max(arr)
right = sum(arr)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    sum_lesson = 0
    for i in range(n):
        if sum_lesson + arr[i] > mid:
            cnt += 1
            sum_lesson = 0
        sum_lesson += arr[i]
    else:
        if sum_lesson:
            cnt += 1
    if cnt <= m:
        right = mid - 1
    else:
        left = mid + 1

print(left)
