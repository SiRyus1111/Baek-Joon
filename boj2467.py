import sys
input = sys.stdin.readline
n = int(input())
sol = list(map(int, input().split(" ")))
start = 0
end = n-1
min = abs(sol[start]+sol[end])
min_start = start
min_end = end
while start<end:
    temp = sol[start] + sol[end]
    if abs(temp) < min:
        min = abs(temp)
        min_start = start
        min_end = end
        if min == 0:
            break
    if temp < 0:
        start += 1
    else:
        end -= 1
print(sol[min_start],sol[min_end],sep=" ")