str = input()
stack = []
temp = 1
ans = 0
for i in range(len(str)):
    if str[i] == "(":
        stack.append("(")
        temp *= 2
    elif str[i] == "[":
        stack.append("[")
        temp *= 3
    elif str[i] == ")":
        if not stack or stack[len(stack) - 1] == "[":
            ans = 0
            break
        if str[i - 1] == "(":
            ans += temp
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[len(stack) - 1] == "(":
            ans = 0
            break
        if str[i - 1] == "[":
            ans += temp
        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(ans)
