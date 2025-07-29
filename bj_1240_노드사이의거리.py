import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

def dfs(cur, target, dist, visited):
    if cur == target:
        return dist
    visited[cur] = True
    for nxt, cost in graph[cur]:
        if not visited[nxt]:
            result = dfs(nxt, target, dist + cost, visited)
            if result != -1:
                return result
    return -1
    
for _ in range(m):
    start, end = map(int, input().split())
    visited = [False] * (n+1)
    print(dfs(start, end, 0, visited))
