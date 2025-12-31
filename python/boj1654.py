import sys
def binary_search(lan,n,start,end): #이분 탐색
    result = 0 #최댓값을 저장할 변수
    while start<=end: 
        mid = (start+end)//2 #평균(가운데의 값)
        cnt = 0 #랜선의 갯수 세기
        for i in lan:
            cnt += i // mid #랜선의 갯수를 평균으로 나눈 값 합하기
        if cnt >= n: #필요한 랜선의 갯수보다 자른 랜선의 갯수가 많거나 같으면
            start = mid + 1 #탐색 범위 변경
            result = mid #지금까지의 최댓값 저장
        else: #아니라면
            end = mid - 1 # 탐색 범위 변경
    return result #가장 마지막 최댓값 반환
    
k, n = map(int, sys.stdin.readline().split(" "))
lan = [int(sys.stdin.readline()) for _ in range(k)]
start = 1
end = max(lan) #가장 긴 랜선의 길이가 end
print(binary_search(lan,n,start,end))