'''
직선도로개수 = 움직인 거리(개수) -> 100원
코너 = 방향 튼 수 -> 500원

0은 비어있음, 1은 벽
출발 0,0 -> 도착 n-1, n-1

더 빨리 도착해도 더 비쌀 수 있음. 따라서 단순히 bfs로 풀면 안됨. 
'''


from collections import deque

def solution(board):
    n = len(board)
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    
    INF = float('inf')
    # 3차원 비용 배열: cost[x][y][방향]
    cost = [[[INF]*4 for _ in range(n)] for _ in range(n)]
    queue = deque()
    
    for i in [1, 3]:  # 시작은 하(1) 또는 우(3) 방향
        cost[0][0][i] = 0
        queue.append((0, 0, i, 0))  # (x, y, 방향, 비용)
    
    while queue:
        x, y, dir, c = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                # 방향 같으면 100, 다르면 600
                new_cost = c + (100 if dir == i else 600)
                
                if cost[nx][ny][i] > new_cost:
                    cost[nx][ny][i] = new_cost
                    queue.append((nx, ny, i, new_cost))
                    
    return min(cost[n-1][n-1])

'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.04ms, 9.33MB)
테스트 2 〉	통과 (0.02ms, 9.42MB)
테스트 3 〉	통과 (0.02ms, 9.32MB)
테스트 4 〉	통과 (0.04ms, 9.29MB)
테스트 5 〉	통과 (0.04ms, 9.3MB)
테스트 6 〉	통과 (0.20ms, 9.3MB)
테스트 7 〉	통과 (0.23ms, 9.32MB)
테스트 8 〉	통과 (0.36ms, 9.27MB)
테스트 9 〉	통과 (0.76ms, 9.27MB)
테스트 10 〉	통과 (0.39ms, 9.27MB)
테스트 11 〉	통과 (61.21ms, 9.32MB)
테스트 12 〉	통과 (1.86ms, 9.25MB)
테스트 13 〉	통과 (0.14ms, 9.27MB)
테스트 14 〉	통과 (0.28ms, 9.34MB)
테스트 15 〉	통과 (1.40ms, 9.42MB)
테스트 16 〉	통과 (1.69ms, 9.3MB)
테스트 17 〉	통과 (7.53ms, 9.33MB)
테스트 18 〉	통과 (4.08ms, 9.3MB)
테스트 19 〉	통과 (40.09ms, 9.33MB)
테스트 20 〉	통과 (0.99ms, 9.28MB)
테스트 21 〉	통과 (0.64ms, 9.27MB)
테스트 22 〉	통과 (0.06ms, 9.34MB)
테스트 23 〉	통과 (0.05ms, 9.19MB)
테스트 24 〉	통과 (0.06ms, 9.31MB)
테스트 25 〉	실패 (0.04ms, 9.21MB)
채점 결과
정확성: 96.0
합계: 96.0 / 100.0
'''
'''
from collections import deque

def solution(board):
    n = len(board)
    # 4방향: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    cost = [[float('inf')] * n for _ in range(n)]
    queue = deque()
    
    # 시작점: (0,0)에서 비용 0
    queue.append((0, 0, -1, 0))  # (x, y, 이전방향, 누적비용)
    cost[0][0] = 0
    
    while queue:
        x, y, prev_dir, c = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                # 방향이 같으면 100, 다르면 600(코너 포함)
                new_cost = c + (100 if prev_dir == -1 or prev_dir == i else 600)
                
                if cost[nx][ny] >= new_cost:
                    cost[nx][ny] = new_cost
                    queue.append((nx, ny, i, new_cost))
    
    return cost[n-1][n-1]
'''