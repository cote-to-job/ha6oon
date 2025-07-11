import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

case_num = 1

def dfs(node, parent):
    global is_tree
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, node)
        elif neighbor != parent:
            is_tree = False  # 사이클 발견

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    tree_count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            is_tree = True
            dfs(i, -1)
            if is_tree:
                tree_count += 1

    if tree_count == 0:
        print(f"Case {case_num}: No trees.")
    elif tree_count == 1:
        print(f"Case {case_num}: There is one tree.")
    else:
        print(f"Case {case_num}: A forest of {tree_count} trees.")
    
    case_num += 1