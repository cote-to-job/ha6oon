import sys
input = sys.stdin.readline

n =int(input())

dp = [0] * (n+1)
dp[1] = 1

if n >= 2:
    dp[2] = 3
    
for i in range(3, n+1):
    # 한칸 채우는 방법 1개, 두칸 채우는 방법 2개 
    dp[i] = dp[i-1] + 2*dp[i-2]
    dp[i] %= 10007
    
print(dp[n])