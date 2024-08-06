clock = list(map(int, input().split(" ")))
cook = int(input())
clock[1] += cook
if clock[1] >= 60:
    clock[0] += int(clock[1] / 60)
    clock[1] = (clock[1] % 60)
if clock[0] >= 24:
    clock[0] -= 24
print(clock[0], clock[1])