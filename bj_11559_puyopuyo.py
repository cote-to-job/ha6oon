from collections import deque

# 입력 받기
board = [list(input()) for _ in range(12)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    color = board[x][y]
    connected = [(x, y)]

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    connected.append((nx, ny))
    
    return connected

def drop():
    for col in range(6):
        stack = []
        for row in range(11, -1, -1):  # 아래에서부터 위로
            if board[row][col] != '.':
                stack.append(board[row][col])
        for row in range(11, -1, -1):
            if stack:
                board[row][col] = stack.pop(0)
            else:
                board[row][col] = '.'

chain_count = 0

while True:
    visited = [[False]*6 for _ in range(12)]
    is_popped = False
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                group = bfs(i, j, visited)
                if len(group) >= 4:
                    is_popped = True
                    for x, y in group:
                        board[x][y] = '.'
    if not is_popped:
        break
    drop()
    chain_count += 1

print(chain_count)
