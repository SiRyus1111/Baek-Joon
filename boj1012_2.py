import sys
input = sys.stdin.readline
t = int(input())
result = []
move = [[0,1],[1,0],[0,-1],[-1,0]]
def dfs(dx,dy):
    stack = list([[dx,dy]])
    while stack:
        nx, ny = stack.pop()
        for jx, jy in move:
            kx = nx + jx
            ky = ny + jy
            if 0<=kx<x and 0<=ky<y and graph[ky][kx] == 1:
                graph[ky][kx] = 0
                stack.append([kx,ky])
for i in range(t):
    x, y, k = map(int, input().split(" "))
    cnt = 0
    graph = [[0] * x for _ in range(y)]
    for j in range(k):
        xx, yy = map(int, input().split(" "))
        graph[yy][xx] = 1
    for j in range(y):
        for k in range(x):
            if graph[j][k] == 1:
                dfs(k,j)
                cnt += 1
    result.append(cnt)
for i in result:
    print(i)