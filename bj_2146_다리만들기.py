from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [1,-1,0,0], [0,0,1,-1]

# 1️⃣ 섬 라벨링
def label_island(x, y, island_id):
    q = deque()
    q.append((x, y))
    graph[x][y] = island_id
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx+dx[k], cy+dy[k]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = island_id
                q.append((nx, ny))

island_id = 2  # 섬 번호는 2부터 시작
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            label_island(i, j, island_id)
            island_id += 1

# 2️⃣ 다리 BFS (섬마다 실행)
def shortest_bridge(start_id):
    dist = [[-1]*n for _ in range(n)]
    q = deque()

    # 시작 섬의 모든 좌표 큐에 넣기
    for i in range(n):
        for j in range(n):
            if graph[i][j] == start_id:
                q.append((i,j))
                dist[i][j] = 0

    # BFS로 확장
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                # 바다일 경우 확장
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                # 다른 섬 도착
                elif graph[nx][ny] > 1 and graph[nx][ny] != start_id:
                    return dist[x][y]  # 다리 길이

    return sys.maxsize

# 3️⃣ 모든 섬에서 BFS 돌려 최소 다리 찾기
answer = sys.maxsize
for k in range(2, island_id):
    answer = min(answer, shortest_bridge(k))

print(answer)
