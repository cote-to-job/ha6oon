'''
*크루스칼 알고리즘:
모든 간선을 비용 순으로 정렬한 뒤, 사이클이 생기지 않도록 간선을 하나씩 선택해 나가며 MST를 만드는 방법

*전체 흐름
1. 모든 간선을 비용 기준으로 정렬한다.
2. 정렬된 간선을 하나씩 보면서:
    - 두 노드가 같은 집합에 속하지 않으면 → 연결하고 비용을 더함.
    - 같은 집합에 속하면 사이클이 생기므로 스킵한다.
3. 간선을 (n-1)개 선택하면 끝! (MST는 항상 간선 수가 n-1)

*유니온 파인드 (Disjoint Set) : 사이클을 만들지 않기 위해서 사용하는 자료구조!
- find(x): x가 속한 집합의 루트 노드 찾기
    루트란? 자기 자신이 부모인 노드 (parent[x] == x)
    만약 parent[x] != x라면, 재귀적으로 parent[parent[x]]를 따라가며 루트를 찾아가.
- union(x, y): x와 y를 같은 집합으로 합치기
    단, 이미 같은 집합이면 합치지 않고 False를 반환해서 사이클을 막아.
    서로 다른 집합이라면, 둘 중 하나의 루트를 다른 쪽에 붙여버림.
'''

def solution(n, costs):
    # 1. 간선 비용 기준 정렬
    costs.sort(key=lambda x: x[2])
    
    # 2. 유니온 파인드 초기화
    parent = [i for i in range(n)] # 각 노드가 자신을 부모로 가짐 (서로 다른 집합)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x]) # 경로 압축
        return parent[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x
            return True
        return False
    
    total = 0
    for a, b, cost in costs:
        if union(a, b): # 연결 안돼 있으면 연결
            total += cost
    return total