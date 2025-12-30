from collections import deque
import sys
sys.setrecursionlimit(10**6)
def dfs(graph,x,y,m,n):
    if x>=m or y>=n or x<0 or y<0:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(graph,x+1,y,m,n)
        dfs(graph,x,y+1,m,n)
        dfs(graph,x-1,y,m,n)
        dfs(graph,x,y-1,m,n)
        return True
    return False
t = int(input())
count = 0
cnt = []
for i in range(t):
    m, n, k = map(int, input().split(" "))
    graph = [[0]*m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split(" "))
        graph[b][a] = 1
    for y in range(n):
        for x in range(m):
            if dfs(graph,x,y,m,n)==True:
                count+=1
    cnt.append(count)
    count = 0
for i in cnt:
    print(i)