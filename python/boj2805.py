import sys
def binary_search(m,start,end,tree): #이분 탐색
    result = 0 #결과(최댓값)을 저장할 변수
    while start<=end:
        mid = (start+end) // 2
        cnt = 0 #나무의 총 길이를 저장할 변수
        for i in tree:
            if i>mid: #나무가 잘리는지(자르는 높이보다 나무가 작진 않은지) 검사
                cnt += (i - mid) #나무 자르기(나무의 길이(i)-자르는 길이(mid))
        if cnt>=m: #자른 나무의 길이가 필요한 나무의 길이보다 길거나 같으면
            result = mid #결과에 자른 길이 저장(최댓값)
            start = mid + 1 #현재의 mid값(최댓값) 이상으로 탐색범위 변경
        else: #아니면
            end = mid - 1 #현재의 mid값 이하로 탐색범위 변경
    return result #다 끝났으면 결과 반환
n, m = map(int, sys.stdin.readline().split(" "))
tree = list(map(int, sys.stdin.readline().split(" "))) #나무 입력받기
start = 0 #시작은 0미터
end = max(tree) #끝은 가장 긴 나무의 길이
print(binary_search(m,start,end,tree)) #출력