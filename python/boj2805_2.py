import sys
input = sys.stdin.readline
n, m = map(int, input().split(" "))
trees = list(map(int, input().split(" ")))
start = 0
end = max(trees)
result = 0
while start<=end:
    mid = (start + end) // 2
    cnt = 0
    for i in trees:
       if i > mid:
           cnt += i - mid
    if cnt >= m:
        start = mid+1
        result = mid
    else:
        end = mid-1
print(result)