def count_paper(matrix, x, y, size, result):
    base = matrix[x][y]
    same = True
    for i in range(x, x+size):
        for j in range(y, y+size):
            if matrix[i][j] != base:
                same = False
                break
        if not same:
            break
    if same:
        result[base] += 1  # 0: white, 1: blue
    else:
        new_size = size // 2
        count_paper(matrix, x, y, new_size, result)
        count_paper(matrix, x+new_size, y, new_size, result)
        count_paper(matrix, x, y+new_size, new_size, result)
        count_paper(matrix, x+new_size, y+new_size, new_size, result)

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0]  # result: white, result: blue
count_paper(matrix, 0, 0, N, result)
for r in result:
    print(r)
