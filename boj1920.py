import sys
def binary_search(array,start,end,target):
    while start<=end:
        mid = (start+end) //2
        if array[mid] == target:
            return True
        elif array[mid]>target:
            end = mid-1
        else:
            start = mid+1
    return False
n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split(" ")))
array.sort()
m = int(sys.stdin.readline())
targets = list(map(int,sys.stdin.readline().split(" ")))
results = [0]*m
for i in range(m):
    k = binary_search(array,0,n-1,targets[i])
    if k==True:
        results[i] = 1
for i in results:
    print(i)