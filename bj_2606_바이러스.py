import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
virus = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    virus[a].append(b)
    virus[b].append(a)

visited = [False] *(n+1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    result = 0
    while queue:
        now = queue.popleft()
        for node in virus[now]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
                result += 1
    return result

result = bfs(1)
print(result)