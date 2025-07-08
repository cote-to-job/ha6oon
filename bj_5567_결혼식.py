import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def bfs(start):
    queue = deque([(start, 0)]) # 노드, 깊이 
    visited[start] = True
    result = 0
    while queue:
        now, depth = queue.popleft()
        if depth >= 2:
            continue
        for node in graph[now]:
            if not visited[node]:
                visited[node] = True  
                queue.append((node, depth + 1))
                result += 1
    return result

result = bfs(1)
print(result)
