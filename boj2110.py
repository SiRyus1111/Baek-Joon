import sys
def binary_search(start,end):
    result = 0
    while start<=end:
        cnt = 1
        mid = (start+end)//2
        last = house[0]
        for i in range(1,len(house)):
            if house[i] >= last + mid:
                cnt += 1
                last = house[i]
        if cnt >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result
n, c = map(int,sys.stdin.readline().split(" "))
house = [int(sys.stdin.readline()) for _ in range(n)]
house.sort()
start = 1
end = house[-1] - house[0]
print(binary_search(start,end))