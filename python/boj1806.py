import sys
input = sys.stdin.readline

n, s = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
start = 0
end = 0
is_possible = False
min_length = len(arr)
temp = arr[start]
while start < n:
    if temp >= s:
        min_length = min(min_length, end - start)
        is_possible = True
        if min_length == 0:
            break
        temp -= arr[start]
        start += 1
    else:
        end += 1
        if end == n:
            break
        temp += arr[end]
if is_possible:
    print(min_length + 1)
else:
    print(0)