import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr = sorted(arr)
for i in range(n):
    print(arr[i])