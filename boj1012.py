from collections import deque
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
    for i in range(m):
        for j in range(n):
            if dfs(graph,i,j,m,n)==True:
                count+=1
    cnt.append(count)
    count = 0
for i in cnt:
    print(i)