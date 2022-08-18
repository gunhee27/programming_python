# 모험가 길드
n = int(input())
data = list(map(int,input().split()))

data.sort()

count = 0
result = 0
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)

# 곱하기 혹은 더하기
data = input()

result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)

# 문자열 뒤집기
data = input();
result0 = 0
result1 = 0

if data[0] == '1':
    result0 += 1
else:
    result1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '0':
            result1 += 1
        else:
            result0 += 1

print(min(result1, result0))

# 만들 수 없는 금액
n = int(input())
data = list(map(int, input().split()))
data.sort()
sum = data[0]
for i in range(1, n):
    if sum >= data[i]:
        sum += data[i]
    else:
        sum += 1
        break
print(sum)

# 볼링공 고르기
n, m = map(int, input().split())
data = list(map(int, input().split()))
array = [0] * (m + 1)
for i in data:
    array[i] += 1

sum = 0
for i in range(1, m + 1):
    n -= array[i]
    sum += n * array[i]

print(sum)

# 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    q = []
    if sum(food_times) <= k:
        return -1
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    length = len(food_times)
    sumV = 0
    previous = 0
    while sumV + length * (q[0][0] - previous) <= k:
        now = heapq.heappop(q)[0]
        sumV += length * (now - previous)
        length -= 1
        previous = now
    result = sorted(q, key = lambda x: x[1])
    return result[(k - sumV) % length][1]