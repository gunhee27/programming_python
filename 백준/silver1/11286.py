from heapq import heappush, heappop
import sys
n = int(input())
heap = []
for _ in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        heappush(heap, (abs(a), a))
    else:
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])