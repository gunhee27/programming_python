#럭키 스트레이트
data = input()
length = len(data)
right = 0
left = 0
for i in range(length):
    if i < (length // 2):
        left += int(data[i])
    else:
        right += int(data[i])
if left == right:
    print("LUCKY")
else:
    print("READY")

#문자열 재정렬
data = input()
result = []
value = 0
for i in data:
    if i.isalpha():
        result.append(i)
    else:
        value += int(i)
result.sort()
result.append(str(value))
print(''.join(result))

# 치킨배달
from itertools import combinations

n, m = map(int, input().split())
house, chicken = [], []
for i in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if c == 1:
            house.append((i, c))
        elif c == 2:
            chicken.append((i, c))

candidates = list(combinations(chicken, m))

def get_sum(candiate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candiate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
