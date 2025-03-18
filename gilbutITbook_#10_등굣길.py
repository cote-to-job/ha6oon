# 제출 코드
def solution(m, n, puddles):
    MOD = 1000000007
    
    dp = [[0 for _ in range(m)] for _ in range(n)]
    puddles_set = {(y-1, x-1) for x, y in puddles}  # puddles를 좌표 보정 후 set으로 변경

    # 초기화 (물이 있으면 이후 경로는 모두 0)
    for r in range(n):
        if (r, 0) in puddles_set:
            break
        dp[r][0] = 1

    for c in range(m):
        if (0, c) in puddles_set:
            break
        dp[0][c] = 1

    # DP 진행
    for r in range(1, n):
        for c in range(1, m):
            if (r, c) in puddles_set: 
                dp[r][c] = 0
            else:
                dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % MOD

    return dp[n-1][m-1]

'''
전의 틀린 코드 피드백
🚩 문제점 분석:
① 웅덩이 처리 방식 오류
현재 puddles 배열의 좌표는 [x, y] 형태로 주어집니다. 하지만 작성하신 코드에서 좌표를 [r+1, c+1]로 비교하고 있습니다.

puddles는 (x, y) 형식이며, 실제 DP에서는 (r, c) 형태로 쓰므로, 비교 시 인덱스가 서로 바뀌어야 합니다.
정확히는 [c+1, r+1]로 비교해야 합니다.
또한 현재는 반복문을 돌 때마다 puddles 리스트에서 찾는 방식(in)을 쓰고 있어 비효율적이므로, set으로 바꾸는 것이 좋습니다.
② 초기화 과정의 문제
물이 있는 위치를 전혀 고려하지 않고 처음부터 dp[0][c] = 1 및 dp[r][0] = 1로 초기화해버립니다.

시작점에서 오른쪽 또는 아래쪽으로만 갈 때, 중간에 웅덩이가 있으면 이후 모든 경로는 막히기 때문에, 초기화 과정에서도 웅덩이를 만나는 순간 이후는 모두 0이 되어야 합니다.'
'''

'''
틀린 코드
def solution(m, n, puddles):
    # 메모이제이션으로 품
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    # dp의 0번째 행과 열에 1을 저장한다.
    for r in range(m):
        dp[r][0] = 1
    for c in range(n):
        dp[0][c] = 1
    # (1, 1) 위치에서 시작
    for r in range(1, m):
        for c in range(1, n):
            if [r+1, c+1] in puddles: # 물웅덩이 처리
                dp[r][c] = 0
            else:
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[m-1][n-1]
'''

'''
좀 더 편리한 코드 (인덱싱 살펴보기)
def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 물에 잠긴 지역 표시
    puddles_set = {(y, x) for x, y in puddles}

    dp[1][1] = 1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if (y, x) in puddles_set:
                dp[y][x] = 0  # 물 웅덩이
            else:
                if y == 1 and x == 1:
                    continue  # 시작점은 이미 1로 초기화됨
                dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD
    
    return dp[n][m]
'''