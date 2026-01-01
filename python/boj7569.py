import sys
from collections import deque
input = sys.stdin.readline
m, n, h = map(int, input().split(" "))
graph = [[[0] * m for _ in range(n)] for _ in range(h)]
keys = []
for i in range(h):
    for j in range(n):
        row = list(map(int, input().split()))
        graph[i][j] = row
        for k in range(m):
            if row[k] == 1:
                keys.append((i, j, k))
def bfs(keys, graph):
    if all(0 not in row for layer in graph for row in layer):
        return 0
    moves = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
    q = deque(keys)
    while q:
        z,y,x = q.popleft()
        for dx, dy, dz in moves:
            kz = z + dz
            ky = y + dy
            kx = x + dx
            if  0<=kz<h and 0<=ky<n and 0<=kx<m and graph[kz][ky][kx] == 0:
                graph[kz][ky][kx] = graph[z][y][x] + 1
                q.append((kz,ky,kx))
    for i in range(h):
        for j in range(n):
            if 0 in graph[i][j]:
                return -1
    maxx = 0
    for i in range(h):
        for j in range(n):
            maxx = max(max(graph[i][j]),maxx)
    return maxx - 1
print(bfs(keys, graph))