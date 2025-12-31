import sys
input = sys.stdin.readline
n, c = map(int,input().split(" "))
house = [int(input()) for _ in range(n)]
house.sort()
start = 1
end = house[-1] - house[0]
result = 0
while start<=end:
    cnt = 1
    mid = (start+end) // 2
    last = house[0]
    for i in range(1,len(house)):
        if house[i] >= last + mid:
            cnt += 1
            last = house[i]
    if cnt >= c:
        result = mid
        start = mid+1
    else:
        end = mid-1
print(result)