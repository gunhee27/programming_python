n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
result = 0
i = 0
while i < len(arr):
    if arr[i] > len(arr):
        break
    else:
        i += arr[i]
        result += 1

print(result)


data = input()
result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    result = max(num + result, num * result)
print(result)

data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)

n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1

result = 0

for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n