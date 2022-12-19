#1183
n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append(a - b)
if n % 2 == 1:
    print(1)
else:
    arr.sort()
    x = len(arr) // 2 - 1
    y = len(arr) // 2
    print(arr[y] - arr[x] + 1)

#1213
n = input()
arr = [0] * 26
for i in n:
    num = ord(i) - 65
    arr[num] += 1
count = 0
answer = ""
temp = ""
for i in range(26):
    if arr[i] % 2 == 1:
        count += 1
        temp = chr(i + 65)
    if arr[i] != 0:
        for j in range(arr[i] // 2):
            answer += chr(i + 65)
if count <= 1:
    rvs = answer[::-1]
    print(answer + temp + rvs)
else:
    print("I'm Sorry Hansoo")

#1024
n, l = map(int, input().split())
count = 0
for i in range(l, 101):
    x = n - (i * (i - 1) / 2)
    if x % i == 0:
        x = int(x / i)
        if x >= -1:
            for j in range(i):
                print(x + j, end = ' ')
                count = 1
            break
if count == 0:
    print(-1)

#1270
n = int(input())
for i in range(n):
    d = dict()
    arr = list(map(int, input().split()))
    num = arr.pop(0)
    max = 0
    key = -1
    for j in arr:
        if j not in d:
            d[j] = 1
        else:
            d[j] += 1
        if d[j] > max:
            max = d[j]
            key = j

    if max > num / 2:
        print(key)
    else:
        print("SYJKGW")

#1058
n = int(input())
g = []
v = [[0] * n for _ in range(n)]
result = 0
for i in range(n):
    g.append(list(input().strip()))
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if g[i][j] == "Y" or (g[i][k] == "Y" and g[k][j] == "Y"):
                v[i][j] = 1
for i in range(n):
    count = 0
    for j in range(n):
        if v[i][j] == 1:
            count += 1
    result = max(result, count)
print(result)

#1124
def is_prime(i):
    if i == 1:
        return False
    num = int(i ** 0.5)
    for k in range(2, num + 1):
        if i % k == 0:
            return False
    return True

def under_prime(arr, num):
    count = 0
    for prime in arr:
        if num == 1:
            break
        while num % prime == 0:
            count += 1
            num //= prime
    return is_prime(count)

a, b = map(int, input().split())
arr = [False, False] + [True]*(b -1)
primes = []
count = 0
for k in range(2, b + 1):
    if arr[k]:
        primes.append(k)
        for j in range(2 * k, b + 1, k):
            arr[j] = False
for i in range(a, b + 1):
    if under_prime(primes, i):
        count += 1
print(count)
