from collections import deque
def solution(n, vertex):

    graph = {i: [] for i in range(1, n+1)}
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    #bfs
    queue = deque([1])  
    distances = [-1] * (n + 1)  
    distances[1] = 0 
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == -1:  
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    max_distance = max(distances)
    print(distances) 
    print(max_distance)
    # max_distance가 distances에 몇갠지 리턴
    return distances.count(max_distance)
