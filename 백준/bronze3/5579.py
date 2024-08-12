arr = [False for i in range(31)]
for _ in range(1, 29):
    n = int(input())
    arr[n] = True

result = [i for i, value in enumerate(arr) if value == False ]
result.remove(0)
for i in result:
    print(i)