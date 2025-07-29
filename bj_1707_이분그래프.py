import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    color = [0] * (v + 1)  # 0: 미방문, 1: 빨강, -1: 파랑

    def bfs(start):
        queue = deque([start])
        color[start] = 1
        while queue:
            now = queue.popleft()
            for neighbor in graph[now]:
                if color[neighbor] == 0:
                    color[neighbor] = -color[now]
                    queue.append(neighbor)
                elif color[neighbor] == color[now]:
                    return False  # 인접 노드와 색이 같음 → 이분 그래프 아님
        return True

    is_bipartite = True
    for i in range(1, v + 1):
        if color[i] == 0:
            if not bfs(i):
                is_bipartite = False
                break

    print("YES" if is_bipartite else "NO")
