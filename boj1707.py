from collections import deque
import sys
def bfs(start,graph,visited):
    q = deque([start])
    visited[start] = 1
    while q:
        m = q.popleft()
        for i in graph[m]:
            if visited[i] == 0:
                visited[i] = -visited[m]
                q.append(i)
            elif visited[i] == visited[m]:
                return False
    return True
k = int(sys.stdin.readline().rstrip())
result = []
for i in range(k):
    v, e = map(int,sys.stdin.readline().split())
    visited = [0]*(v+1)
    graph = [[] for _ in range(v+1)]
    con = True
    for i in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,v+1):
        if bfs(i,graph,visited) == False:
            con = False
            break
    if con == False:
        result.append("NO")
    else:
        result.append("YES")
for i in range(k):
    print(result[i])