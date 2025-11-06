from collections import deque
import sys
def bfs(x,y,graph,n,m): #bfs
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]:
            fx = x+dx
            fy = y+dy
            if 0<=fx<m and 0<=fy<n and graph[fy][fx]==1:
                graph[fy][fx] = graph[y][x] + 1
                q.append((fx,fy))
    return graph[n-1][m-1]
n, m = map(int, sys.stdin.readline().split(" "))
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
print(bfs(0,0,graph,n,m))