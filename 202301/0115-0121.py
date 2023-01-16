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