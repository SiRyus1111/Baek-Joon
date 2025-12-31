import sys
def fibo(n,dp): #DP
    if n==0: #기저값
        return (1,0)
    if n==1: #기저값
        return (0,1)
    if dp[n] != (0,0): #이미 값이 저장되어 있으면
        return dp[n] #저장된 값 반환
    a1, b1 = fibo(n-1,dp) #이전의 값들로 현재 값 계산
    a2, b2 = fibo(n-2,dp) #이전의 값들로 현재 값 계산
    dp[n] = (a1+a2,b1+b2) #현재 값 저장
    return dp[n] #값이 저장되어 있지 않으면 이전의 값들로 계산한 값 반환
dp = [(0,0) for _ in range(41)] #DP배열
dp[0] = (1,0) #기저값
dp[1] = (0,1) #기저값
fibo(40,dp) #미리 계산
t = int(sys.stdin.readline()) #테스트 케이스 수
result = [] #결과를 저장할 배열
for i in range(t):
    n = int(sys.stdin.readline()) #n 입력
    result.append(dp[n]) #결과 저장
for i, o in result: #출력
    print(i,o,sep=" ")