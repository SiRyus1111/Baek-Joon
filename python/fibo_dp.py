import sys
def fibo(n,dp):
    global cnt
    cnt += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fibo(n-1,dp) + fibo(n-2,dp)
        return dp[n]
cnt = 0
dp = [-1] * 41
dp[0] = 0
dp[1] = 1
fibo(40,dp)
print(cnt)