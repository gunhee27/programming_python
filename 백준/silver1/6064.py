T = int(input())
for _ in range(T):
    m,n,x,y = map(int, input().split())
    ans = -1
    while x <= m * n:
        if (x - y) % n == 0:
            ans = x
            break
        x += m
    print(ans)
