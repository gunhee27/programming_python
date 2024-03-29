# 시간초과 된 풀이
# TODO 시간 줄이기

arr = list(input().rstrip())
m = int(input())
cursor = len(arr)
for i in range(m):
    todo = input().split()
    if len(todo) > 1 :
        arr.insert(cursor, todo[1])
        cursor += 1
    else:
        if todo[0] == 'L' and cursor > 0:
            cursor -= 1
        elif todo[0] == 'D' and cursor < len(arr):
            cursor += 1
        elif todo[0] == 'B' and cursor > 0:
            arr.pop(cursor - 1)
            cursor -= 1
for j in arr:
    print(j, end='')

# 정답 풀이

import sys

arr = list(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline())
right = []
for i in range(m):
    todo = list(sys.stdin.readline().split())
    if todo[0] == 'L':
        if arr:
            right.append(arr.pop())
    elif todo[0] == 'D':
        if right:
            arr.append(right.pop())
    elif todo[0] == 'B':
        if arr:
            arr.pop()
    else:
        arr.append(todo[1])
print("".join(arr + list(reversed(right))))


