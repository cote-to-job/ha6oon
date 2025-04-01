# DP 최적화, dp[b] = 해당 B 흔적합일 때 최소 A 흔적합
# O(k * n * m) = 40 * 120 * 120 = 576,000

def solution(info, n, m):
    # 초기값: B의 흔적 합에 대한 최소 A의 흔적 합
    dp = {0: 0}  # key: b_sum (B의 흔적 누적값), value: 최소 A의 흔적 합

    for a_trace, b_trace in info:
        next_dp = dict()
        for b_sum, a_sum in dp.items():
            # Case 1: 현재 물건을 A가 훔치는 경우
            new_a_sum = a_sum + a_trace
            new_b_sum = b_sum
            if new_a_sum < n and new_b_sum < m:
                if new_b_sum not in next_dp or next_dp[new_b_sum] > new_a_sum:
                    next_dp[new_b_sum] = new_a_sum

            # Case 2: 현재 물건을 B가 훔치는 경우
            new_a_sum = a_sum
            new_b_sum = b_sum + b_trace
            if new_a_sum < n and new_b_sum < m:
                if new_b_sum not in next_dp or next_dp[new_b_sum] > new_a_sum:
                    next_dp[new_b_sum] = new_a_sum

        dp = next_dp  # 다음 단계로 갱신

    # 가능한 결과 중 A의 흔적 합의 최솟값 찾기
    return min(dp.values()) if dp else -1


'''
# 최적화 방법 안떠올라짐. 일단 완전탐색으로 구현해보기.-> 테케는 맞는데 채점 실패.(40점)
# product([0,1], repeat=k)는 경우의 수가 2^k,즉, 최악의 경우 2^40 ≈ 1조개의 조합이 생김

from itertools import product

def solution(info, n, m):
    k = len(info)
    min_a_trace = float('inf')
    
    for case in product([0, 1], repeat=k):  # 중복순열(0: A가 훔침, 1: B가 훔침)
        a_trace, b_trace = 0, 0
        for i in range(k):
            if case[i] == 0:
                a_trace += info[i][0]
            else:
                b_trace += info[i][1]
        
        if a_trace < n and b_trace < m:
            min_a_trace = min(min_a_trace, a_trace)
    
    return min_a_trace if min_a_trace != float('inf') else -1
'''