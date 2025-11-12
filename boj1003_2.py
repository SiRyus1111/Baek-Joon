import sys
def fibo(n,dp):
    if n==0:
        return (1,0)
    if n==1:
        return (0,1)
    if dp[n] != (0,0):
        return dp[n]
    a1, b1 = fibo(n-1,dp)
    a2, b2 = fibo(n-2,dp)
    dp[n] = (a1+a2,b1+b2)
    return dp[n]
dp = [(0,0) for _ in range(41)]
fibo(40,dp)
t = int(sys.stdin.readline())
result = []
for i in range(t):
    k = int(sys.stdin.readline())
    result.append(dp[k])
for i, o in result:
    print(i,o,sep=" ")