import sys
n = int(sys.stdin.readline())
arr = [[0,0]*n]
last = 0
count = 0
for i in range(n):
    arr[i][0], arr[i][1] = map(int,sys.stdin.readline().split(" "))
arr.sort(key=lambda x:x[1])
for i in range(n):
    if(arr[i][0]>=last):
        last = arr[i][1]
        count+=1
print(count)