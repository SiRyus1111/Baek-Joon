import sys
n = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split(" ")))
city = list(map(int, sys.stdin.readline().split(" ")))
oil = city[0]
sum = 0
for i in range(n-1):
    if oil > city[i]:
        oil = city[i]
    sum += oil * road[i]
print(sum)