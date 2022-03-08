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