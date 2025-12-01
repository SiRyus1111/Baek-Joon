import sys
def binary_search(start,end,m):
    result = 0
    while start<=end:
        cnt = 0
        mid = (start+end)//2
        for i in snacks:
            cnt += i//mid
        if cnt>=m:
            result = mid
            start = mid+1
        else:
            end = mid-1
    return result
m, n = map(int,sys.stdin.readline().split(" "))
snacks = list(map(int,sys.stdin.readline().split(" ")))
start = 1
end = max(snacks)
print(binary_search(start,end,m))