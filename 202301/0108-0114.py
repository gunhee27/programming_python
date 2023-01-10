###############################
# 0109
###############################
# 2805
import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left, right = 1, max(arr)
while left <= right:
    mid = (left + right) // 2
    s = 0
    for i in arr:
        if i >= mid:
            s = s + (i - mid)
    if s < m:
        right = mid - 1
    else:
        left = mid + 1
print(right)

###############################
# 0110
###############################
# 1541
arr = input().split('-')
result = []
for i in arr:
    if i.find('+') >= 0:
        num = 0
        temp = i.split('+')
        for j in temp:
            num += int(j)
        result.append(num)
    else:
        result.append(int(i))
print(result[0] - sum(result[1:]))

# 1654
k, n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))

left = 1
right = max(arr)
while left <= right:
    mid = (left + right) // 2
    s = 0
    for i in arr:
        s += (i // mid)
    if s >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)