import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    i = int(input())
    if i == 0:
        if stack:
            stack.pop()
        else:
            pass
    else:
        stack.append(i)
print(sum(stack))