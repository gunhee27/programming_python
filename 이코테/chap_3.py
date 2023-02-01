# 연습문제
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(coin)

# 큰 수의 법칙_단순하게
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0: break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 큰 수의 법칙_효율
n, m, k = map(int,input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(n / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)

#숫자 카드 게임
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 내 풀이
    data.sort()
    if result < data[0]:
        result = data[0];
    #해설지 풀이
    min_value = min(data)
    result = max(result, min_value)
print(result)

# 1이 될 때까지_나의 풀이
n, k = map(int, input().split())
count = 0
while n != 1:
    n -= 1
    count += 1
    if n % k == 0:
        n /= k
        count += 1
print(count)

# 1이 될 때까지_해설지 풀이
n, k = map(int, input().split())
count = 0
while True:
    target = (n // k) * k
    count += (n - target)
    n = target
    if n < k:
        break
    count += 1
    n //= k
count += (n - 1)
print(count)