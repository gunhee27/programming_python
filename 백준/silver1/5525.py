n = int(input())
m = int(input())
s = input()
i = 0
count = 0
answer = 0
while i < m:
    if s[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == n:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0
print(answer)