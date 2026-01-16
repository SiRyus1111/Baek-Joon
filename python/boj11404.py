import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        graph[i][i] = 0
        if graph[i][k] == INF:
            continue
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for from_node in range(1, n+1):
    for to_node in range(1, n+1):
        
        print(0 if graph[from_node][to_node] == INF else graph[from_node][to_node], end = " ")
    print()