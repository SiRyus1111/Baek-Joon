import sys
input = sys.stdin.readline

n = int(input())

wine = [int(input()) for _ in range(n)]
dp = [[0,0,0] for _ in range(n)]

if n == 1:
    print(wine[0])
    sys.exit()
if n == 2:
    print(wine[0] + wine[1])
    sys.exit()

dp[0][0], dp[0][1], dp[0][2] = 0 , wine[0], 0
dp[1][0], dp[1][1], dp[1][2] = dp[0][1] + wine[1], wine[1], max(dp[0])
dp[2][0], dp[2][1], dp[2][2] = dp[1][1] + wine[2], dp[1][2] + wine[2], max(dp[1])


for i in range(3,n):
    dp[i][0], dp[i][1], dp[i][2] = dp[i-1][1] + wine[i], dp[i-1][2] + wine[i], max(dp[i-1])

print(max(dp[n-1]))