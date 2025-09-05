import sys
input = sys.stdin.readline

n = int(input())
count = 0

for _ in range(n):
    words = input().strip()
    stack = []
    
    for w in words:
        if len(stack) == 0:
            stack.append(w)
        elif len(stack) != 0 and stack[-1] == w:
            stack.pop()
        elif len(stack) != 0 and stack[-1] != w:
            stack.append(w)
    if len(stack) == 0:
        count += 1
print(count)