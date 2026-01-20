import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left = 0
right = n-1

ans_l = 0
ans_r = 0

cur_min = sys.maxsize

while left < right:
    mixed = liquid[left] + liquid[right]
    temp = abs(mixed)

    if mixed == 0:
        ans_l = left
        ans_r = right
        break
    
    if cur_min > temp:
        ans_l = left
        ans_r = right
        cur_min = temp
    
    if mixed > 0:
        right -= 1
    
    else:
        left += 1

print(liquid[ans_l], liquid[ans_r], sep=" ")