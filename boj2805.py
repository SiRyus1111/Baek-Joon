import sys
def binary_search(m,start,end,tree):
    result = 0
    while start<=end:
        mid = (start+end) // 2
        cnt = 0
        for i in tree:
            if i>mid:
                cnt += (i - mid)
        if cnt>=m:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result
n, m = map(int, sys.stdin.readline().split(" "))
tree = list(map(int, sys.stdin.readline().split(" ")))
start = 0
end = max(tree)
print(binary_search(m,start,end,tree))