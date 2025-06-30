import sys
n = int(sys.stdin.readline().strip())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline().strip()))

l.sort()

for i in range(n):
    print(l[i])