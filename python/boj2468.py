import sys
import copy
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
graph = []
max = 0
result = 1
move = [[0,1],[0,-1],[1,0],[-1,0]]
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split(" ")))
    graph.append(arr)
    for j in arr:
        if j > max:
            max = j
def dfs(k,x,y):
    for dy, dx in move:
        nx = x + dx
        ny = y + dy
        if 0<=nx<n and 0<=ny<n and visited[ny][nx] == 0:
            if graph[ny][nx] > k:
                visited[ny][nx] = 1
                dfs(k,nx,ny)
for i in range(max):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                cnt += 1
                visited[j][k] = 1
                dfs(i,k,j)
    result = max(result, cnt)
print(result)