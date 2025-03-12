def solution(triangle):
    n = len(triangle)
    
    # DP로 경로의 합을 저장하며 내려갑니다.
    for i in range(1, n):
        for j in range(len(triangle[i])):
            # 가장 왼쪽 칸인 경우 바로 위의 숫자만 더함
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            # 가장 오른쪽 칸인 경우 왼쪽 위의 숫자만 더함
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            # 중간 칸들은 두 개의 숫자 중 더 큰 것을 더함
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    # 마지막 줄에서 최대값 반환
    return max(triangle[-1])