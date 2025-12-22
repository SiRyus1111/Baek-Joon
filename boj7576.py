import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split(" "))
graph = [0] * n
for i in range(n):
    graph[i] = list(map(int, input().split(" ")))
keys = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            keys.append((i,j))
def bfs(graph, keys):
    if all(0 not in row for row in graph):
        return 0
    q = deque(keys)
    while q:
        y, x = q.popleft()
        for fx, fy in [[0,1],[1,0],[0,-1],[-1,0]]:
            dx = x + fx
            dy = y + fy
            if 0<=dx<m and 0<=dy<n and graph[dy][dx] == 0:
                graph[dy][dx] = graph[y][x] + 1
                q.append((dy,dx))
    for i in range(n):
        if 0 in graph[i]:
            return -1
    maxx = 0
    for i in range(n):
        maxx = max(max(graph[i]),maxx)
    return maxx - 1
print(bfs(graph,keys))