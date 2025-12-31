import sys
n = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split(" ")))
m = int(sys.stdin.readline())
find = list(map(int,sys.stdin.readline().split(" ")))
card.sort()
result = [0] * m
def binary_search(start,end):
    for i in find:
        while start<=end:
            mid = (start+end) // 2
            if card[mid] == i:
                break
            elif card[mid] < i:
                start = mid + 1
            else:
                end = mid - 1
        
        
