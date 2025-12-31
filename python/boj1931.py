import sys
n = int(sys.stdin.readline().strip())
arr = [[0,0] for _ in range(n)]
last = 0
count = 0
for i in range(n):
    arr[i][0], arr[i][1] = map(int,sys.stdin.readline().strip().split())
arr.sort(key=lambda x:(x[1],x[0]))
for i in range(n):
    if(arr[i][0]>=last):
        last = arr[i][1]
        count+=1
print(count)