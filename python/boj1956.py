import sys
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())

graph = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1,v+1):
    
    for i in range(1,v+1):
        
        if graph[i][k] == INF:
            continue
        
        for j in range(1,v+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
ans = sys.maxsize
for i in range(v+1):
    ans = min(ans,graph[i][i])
print(-1 if ans == INF else ans)