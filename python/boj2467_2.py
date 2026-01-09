import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split(" ")))
start = 0
end = n-1
ans = abs(liquid[start] + liquid[end])
min_index = [start, end]

while start < end:
    mixed = liquid[start] + liquid[end]
    mixed_ABS = abs(mixed)
    if mixed_ABS < ans:
        min_index = [start, end]
        ans = mixed_ABS
        if ans == 0:
            break
    if mixed < 0:
        start += 1
    else:
        end -= 1

print(liquid[min_index[0]], liquid[min_index[1]], sep=" ")