def quad_tree(matrix, x, y, size):
    base = matrix[x][y]
    same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != base:
                same = False
                break
        if not same:
            break
    if same:
        return base
    else:
        half = size // 2
        return "(" + \
            quad_tree(matrix, x, y, half) + \
            quad_tree(matrix, x, y + half, half) + \
            quad_tree(matrix, x + half, y, half) + \
            quad_tree(matrix, x + half, y + half, half) + \
            ")"

N = int(input())
matrix = [input().strip() for _ in range(N)]
print(quad_tree(matrix, 0, 0, N))
'''
# 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
x =0, y=0 ,half =2            
00 01 | 02 03
10 11 | 12 13
-------------
20 21 | 22 23
30 31 | 32 33
'''
