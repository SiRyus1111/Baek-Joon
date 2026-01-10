import sys
input = sys.stdin.readline

n = int(input())
arr = [[0,0] for _ in range(n)]
for i in range(n):
    arr[i][0], arr[i][1] = map(int, input().split(" "))

dp = [0 for _ in range(n+1)]
for i in range(n):
    finish = i + arr[i][0]
    for j in range(finish, n+1):
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]
print(dp[-1])