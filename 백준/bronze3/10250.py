import sys
T = int(input())
for _ in range(T):
    h, w, n = map(int,sys.stdin.readline().split())
    if n % h == 0:
        floor = h
        room = n // h
    else:
        floor = n % h
        room = n // h + 1
    print(floor * 100 + room)