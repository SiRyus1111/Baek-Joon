import sys
n = int(sys.stdin.readline())

dp = [None] * n

for i in range(n):
    arr = list(map(int, sys.stdin.readline().split(" ")))
    dp[i] = arr

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][1],dp[i-1][0]) + dp[i][2]
    
print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))