from collections import deque, defaultdict

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False]*m for _ in range(n)]
    oil_id = 1 
    oil_info = {}  
    column_oil_map = defaultdict(set)  

    # BFS로 덩어리 탐색
    def bfs(x, y, oil_id):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        size = 1
        cols = set([y])
        land[x][y] = oil_id  

        while q:
            cx, cy = q.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = cx+dx, cy+dy
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and land[nx][ny]==1:
                    visited[nx][ny] = True
                    land[nx][ny] = oil_id
                    q.append((nx, ny))
                    size += 1
                    cols.add(ny)

        oil_info[oil_id] = size
        for col in cols:
            column_oil_map[col].add(oil_id)

    # 1. 덩어리 탐색
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j, oil_id)
                oil_id += 1

    # 2. 각 열에서 뽑을 수 있는 최대 석유량 계산
    max_oil = 0
    for col in range(m):
        total = sum(oil_info[oid] for oid in column_oil_map[col])
        max_oil = max(max_oil, total)

    return max_oil
