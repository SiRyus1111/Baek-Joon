import sys
def binary_search(lan,n,start,end):
    result = 0
    while start<=end:
        mid = (start+end)//2
        cnt = 0
        for i in lan:
            cnt += i // mid
        if cnt >= n:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result
    
k, n = map(int, sys.stdin.readline().split(" "))
lan = [int(sys.stdin.readline()) for _ in range(k)]
start = 1
end = max(lan)
print(binary_search(lan,n,start,end))
