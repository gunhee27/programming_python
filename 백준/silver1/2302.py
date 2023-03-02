n = int(input())
m = int(input())
arr = []
for _ in range(m):
    arr.append(int(input()))
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1
if m > 0:
    temp = 0
    for i in range(m):
        answer *= dp[arr[i] - 1 - temp]
        temp = arr[i]
    answer *= dp[n - temp]
else:
    answer = dp[n]
print(answer)