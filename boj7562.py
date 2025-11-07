from collections import deque
import sys
move = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
def bfs(x,y,n,kx,ky):
    if x ==kx and y == ky:
        return 0
    graph = [[-1]*n for _ in range(n)]
    graph[y][x] = 0
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        k = graph[y][x]
        for fx, fy in move:
            dx = x+fx
            dy = y+fy
            if 0<=dx<n and 0<=dy<n and graph[dy][dx]==-1:
                graph[dy][dx] = k+1
                if dy == ky and dx == kx:
                    return graph[dy][dx]
                q.append((dx,dy))
t = int(sys.stdin.readline().rstrip())
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    x, y = map(int, sys.stdin.readline().split(" "))
    kx, ky = map(int, sys.stdin.readline().split(" "))
    print(bfs(x,y,n,kx,ky))