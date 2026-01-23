import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start = 1
end = n * n
ans = 0

# k번째 = cnt번째
# cnt = mid 이하의 수 갯수
# cnt가 k보다 크면 mid는 너무 크다
# cnt가 k보다 작으면 mid는 너무 작다
# 너무 어렵다 진짜
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in range(1, n+1):
        cnt += min((mid//i), n) # 한 행의 최대 길이는 n이다. 그러므로 한 행에서 mid보다 작은 수의 갯수는 최대 n개이다.
    if cnt >= k: # cnt가 k보다 크거나 같으면 같은 문제를 공유한다. 
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)