def solution(players, m, k):
    answer = 0
    dp = [0] * 24     #시간에 따른 서버

    for i in range(24):
        # 현재 시간 i에 필요한 추가 서버 수
        required = players[i] // m
        # 이미 활성화된 추가 서버 수와 비교하여 부족하면 추가 증설
        if dp[i] < required:
            add = required - dp[i]
            answer += add
            # 추가한 서버는 시간 i부터 i+k-1까지 운영
            for j in range(i, min(i+k, 24)):
                dp[j] += add
    return answer