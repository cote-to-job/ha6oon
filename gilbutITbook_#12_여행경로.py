from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    for a in graph:
        graph[a].sort(reverse=True)
    answer = []
    
    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop()) 
        answer.append(airport)
    dfs("ICN")
    
    return answer[::-1]
'''
# heapq로 풀어도됨
def solution(tickets):
    from collections import defaultdict
    import heapq

    # 그래프 생성
    graph = defaultdict(list)
    for a, b in tickets:
        heapq.heappush(graph[a], b)  # 알파벳 순을 위해 heap 사용

    route = []

    def dfs(airport):
        while graph[airport]:
            next_airport = heapq.heappop(graph[airport])
            dfs(next_airport)
        route.append(airport)

    dfs("ICN")
    return route[::-1]  # 역순으로 결과 반환

'''