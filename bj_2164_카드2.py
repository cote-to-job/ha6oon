import sys
input = sys.stdin.readline
from collections import deque
queue = deque()
n = int(input())
q = deque(range(1, n + 1))
while len(q) > 1:
    q.popleft()
    first = q.popleft()
    q.append(first)
    
#print(q)
answer = q.pop()
print(answer)