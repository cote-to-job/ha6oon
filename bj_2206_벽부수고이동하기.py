import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

# dist[r][c][b] = (r,c)에 벽을 b번 부순 상태로 도달했을 때의 최단 거리
# 0: 아직 안 부숨, 1: 한 번 부숨
dist = [[[0]*2 for _ in range(M)] for __ in range(N)]

dq = deque()
dq.append((0, 0, 0))         # (r, c, broke)
dist[0][0][0] = 1            # 시작 칸도 포함하므로 1부터

dirs = [(-1,0),(1,0),(0,-1),(0,1)]

while dq:
    r, c, b = dq.popleft()

    # 목표 지점
    if r == N-1 and c == M-1:
        print(dist[r][c][b])
        break

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            # 다음 칸이 빈 칸(0) -> 상태 유지
            if grid[nr][nc] == 0 and dist[nr][nc][b] == 0:
                dist[nr][nc][b] = dist[r][c][b] + 1
                dq.append((nr, nc, b))
            # 다음 칸이 벽(1)이고 아직 안 부쉈다면 -> 부수고 이동(b -> 1)
            elif grid[nr][nc] == 1 and b == 0 and dist[nr][nc][1] == 0:
                dist[nr][nc][1] = dist[r][c][b] + 1
                dq.append((nr, nc, 1))
else:
    # while을 정상 종료(= break 없이)하면 도달 불가
    print(-1)
