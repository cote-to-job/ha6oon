def bottom_up(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    return dp[n]

# 실행
n = int(input())
print(bottom_up(n))


import sys
sys.setrecursionlimit(10**7) # 재귀 함수가 호출될 수 있는 최대 깊이를 설정

def top_down(n, dp):
    if n == 1:
        return 0
    if dp[n] != -1:
        return dp[n]
    
    # 1을 뺀 경우
    dp[n] = top_down(n - 1, dp) + 1
    
    if n % 2 == 0:
        dp[n] = min(dp[n], top_down(n // 2, dp) + 1)
    if n % 3 == 0:
        dp[n] = min(dp[n], top_down(n // 3, dp) + 1)
    
    return dp[n]

'''
# 실행
n = int(input())
dp = [-1] * (n + 1)
print(top_down(n, dp))
'''