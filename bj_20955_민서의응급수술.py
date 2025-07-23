import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v] = True
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)

components = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        components += 1

# 최소 연산 횟수 = (사이클 제거) + (연결 요소 - 1)
# 사이클 수 = M - (N - components)
cycles = M - (N - components)
print(cycles + (components - 1))