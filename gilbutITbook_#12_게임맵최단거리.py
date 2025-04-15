from collections import deque
def solution(maps):
    # bfs
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    queue = deque()
    queue.append((0, 0, 1)) # 좌표와 거리
    visited[0][0] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y, distance = queue.popleft()
        
        if x == n-1 and y == m-1 :
            return distance
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, distance + 1))
    return -1