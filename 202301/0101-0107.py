###############################
# 0101
###############################
# 1182
from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(1, n + 1):
    temp = list(combinations(arr, i))
    for j in temp:
        if sum(j) == s:
            count += 1
print(count)

# 1198
from itertools import combinations
n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

temp = list(combinations(arr, 3))
maxTri = 0
for i in temp:
    x = i[0][0] * i[1][1] + i[1][0] * i[2][1] + i[2][0] * i[0][1]
    y = i[1][0] * i[0][1] + i[2][0] * i[1][1] +i[0][0] * i[2][1]
    result = abs(x - y) * 0.5
    if result > maxTri:
        maxTri = result
print(maxTri)

###############################
# 0102
###############################
# 1254
def dual(s):
    for i in range(len(s)):
        if s[i] == s[len(s) - i - 1]:
            continue
        else:
            return 0
    return 1

s = input()
if dual(s) == 1:
    print(len(s))
else:
    for i in range(len(s)):
       temp = s + s[:i][::-1]
       if dual(temp) == 1:
           print(len(temp))
           break