n = int(input())
prime = [True] * 1000001
prime[0] = False
prime[1] = False
m = int(1000001 ** 0.5)

for i in range(2, m + 1):
    if prime[i]:
        for j in range(i + i, 1000001, i):
            prime[j] = False


def palindrome(x):
    x = str(x)
    temp = x[:: -1]
    if x == temp:
        return True
    else:
        return False

flag = True
for i in range(n, 1000001):
    if str(i) == str(i)[::-1]:
        if prime[i]:
            flag = False
            print(i)
            break
if flag:
    print(1003001)
