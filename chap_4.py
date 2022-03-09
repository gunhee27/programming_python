# 상하좌우
N = int(input())
plans = input().split()
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for i in plans:
    for j in range(len(move)):
        if i == move[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    x, y = nx, ny

print(x, y)

# 시각
h = int(input())
count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

# 왕실의 나이트
temp = input()
row = int(temp[1])
column = int(ord(temp[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
result = 0
for i in steps:
    next_row = row + i[0]
    next_col = column + i[1]
    if next_row >= 1 & next_row <= 8 & next_col >= 1 & next_col <= 8:
        result = result + 1
print(result)

# 게임 개발
N, M = map(int, input().split())
A, B, d = map(int, input().split())
map = [[0] * M for _ in range(N)]
map[A][B] = 1
array = []
for i in range(N):
    array.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


count = 1
turn_time = 0
while True:
    turn_left()
    nx = A + dx[d]
    ny = B + dy[d]
    if map[nx][ny] == 0 and array[nx][ny] == 0:
        map[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)