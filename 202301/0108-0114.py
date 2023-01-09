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