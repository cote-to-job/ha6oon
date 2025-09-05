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
        result[base+1] += 1  # -1→0, 0→1, 1→2
    else:
        new_size = size // 3
        for dx in range(3):
            for dy in range(3):
                count_paper(matrix, x+dx*new_size, y+dy*new_size, new_size, result)

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = [0,0,0]  # result for -1, result for 0, result for 1
count_paper(matrix, 0, 0, N, result)
for r in result:
    print(r)