n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in range(m):
    temp = arr[0] + arr[1]
    arr[0], arr[1] = temp, temp
    arr.sort()

print(sum(arr))

import sys
import heapq
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
heapq.heapify(arr)

for i in range(m):
    card1 = heapq.heappop(arr)
    card2 = heapq.heappop(arr)
    heapq.heappush(arr, card1 + card2)
    heapq.heappush(arr, card1 + card2)
print(sum(arr))
