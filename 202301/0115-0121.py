###############################
# 0116
###############################
# 1874
n = int(input())
arr = []
answer = []
cur = 1
flag = 0
for i in range(n):
    a = int(input())
    while cur <= a:
        arr.append(cur)
        answer.append("+")
        cur += 1
    if arr[-1] == a:
        arr.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    for i in answer:
        print(i)

###############################
# 0117
###############################
# 10799
n = input()
stack = []
count = 0
for i in range(len(n)):
    if n[i] == '(':
        stack.append('(');
    else:
        stack.pop()
        if n[i - 1] == '(':
            count += len(stack)
        else:
            count += 1
print(count)

# 6603
from itertools import combinations
while 1:
    n = list(map(int, input().split()))
    if n[0] == 0: break
    k = n[0]
    arr = n[1:]
    result = list(combinations(arr, 6))
    for i in result:
        for j in i:
            print(j, end=' ')
        print()
    print()