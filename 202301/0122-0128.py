###############################
# 0122
###############################
# 1931
n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])
arr.sort(key = lambda x: (x[1], x[0]))
cnt = 1
end = arr[0][1]
for i in range(1, n):
    if arr[i][0] >= end:
        cnt += 1
        end = arr[i][1]
print(cnt)