import sys
t = int(sys.stdin.readline()) #테스트 케이스 수
dp = [[0,0] for _ in range(41)] #DP배열
dp[0] = [1,0] #기저값
dp[1] = [0,1] #기저값
result = [] #결과를 저장할 배열
for i in range(2,41): #40번째 피보나치 수까지 미리 DP계산 (0<=n<=40)
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]
for i in range(t):
    n = int(sys.stdin.readline()) #n 입력받기
    result.append(dp[n]) #결과 배열에 더하기
for i,o in result: #출력
    print(i,o,sep=" ")