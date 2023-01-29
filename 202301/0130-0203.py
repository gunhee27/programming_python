###############################
# 0129
###############################
# 14888
n = int(input())
arr = list(map(int, input().split()))

a, b, c, d = map(int, input().split())
maxi = -1e9
mini = 1e9

def dfs(d, total, add, minus, multi, div):
    global maxi, mini
    if d == n:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return

    if add:
        dfs(d + 1, total + arr[d], add - 1, minus, multi, div)
    if minus:
        dfs(d + 1, total - arr[d], add, minus - 1, multi, div)
    if multi:
        dfs(d + 1, total * arr[d], add, minus, multi - 1, div)
    if div:
        dfs(d + 1, int(int(total) / arr[d]), add, minus, multi, div - 1)


dfs(1, arr[0], a, b, c, d)
print(maxi)
print(mini)

#1991
n = int(input())
tree = {}
for i in range(n):
    root, left, right= input().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')