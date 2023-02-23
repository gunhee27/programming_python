a, b = map(int, input().split())

def sol(a, b):
    while b:
        temp = a % b
        a = b
        b = temp
    return a

print('1' * sol(a, b))