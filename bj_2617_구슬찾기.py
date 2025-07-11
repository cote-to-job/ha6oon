'''
중간이 될 수 없는 조건
1. 어떤 구슬보다 무거운 구슬의 수가 (N+1)//2 이상인 경우 → 중간보다 무거우니까 중간일 수 없음
2. 어떤 구슬보다 가벼운 구슬의 수가 (N+1)//2 이상인 경우 → 중간보다 가벼우니까 중간일 수 없음
'''

import sys
input = sys.stdin.readline
# 그래프에 넣고, 각 정점에서 각 dfs를 해서 깊이가 중간값 이상일 경우 result+1 해줌 
# 무거운 구슬, 가벼운 구술에 대해 각 방향그래프를 만든다 -> 두개의 방향그래프 

n, m = map(int, input().split())

heavier_graph = [[] for _ in range(n+1)]
lighter_graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    heavier_graph[a].append(b)  # a > b
    lighter_graph[b].append(a)  # b < a
    
mid = (n + 1) // 2
result = 0

def dfs(graph, node, visited):
    count = 0
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            count += 1
            count += dfs(graph, neighbor, visited)
    return count


for i in range(1, n + 1):
    visited_heavy = [False] * (n + 1)
    visited_light = [False] * (n + 1)

    visited_heavy[i] = True
    visited_light[i] = True

    lighter_cnt = dfs(heavier_graph, i, visited_heavy)  # i보다 가벼운 애들
    heavier_cnt = dfs(lighter_graph, i, visited_light)  # i보다 무거운 애들

    if lighter_cnt >= mid or heavier_cnt >= mid:
        result += 1

print(result)