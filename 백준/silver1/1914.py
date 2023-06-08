n = int(input())
def hanoi(n, start, end):
    global count
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, 6 - start - end)
    print(start, end)
    hanoi(n - 1, 6 - start - end, end)

result = 2 ** n - 1
print(result)
if n <= 20:
    hanoi(n, 1, 3)