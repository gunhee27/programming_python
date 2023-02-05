a, b, c = map(int, input().split())
def multiple(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (multiple(a, b // 2, c) ** 2) % c
    else:
        return ((multiple(a, b // 2, c) ** 2) * a) % c
print(multiple(a, b, c))