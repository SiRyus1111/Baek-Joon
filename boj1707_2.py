import sys
sys.setrecursionlimit(10**6)
def dfs(v,graph,visited,k):
    visited[v] = k
    for i in graph[v]:
        if visited[i] == 0:
            if not dfs(i,graph,visited,-k):
                return False
        elif visited[i] == visited[v]:
            return False
    return True
t = int(sys.stdin.readline().rstrip())
result = []
for i in range(t):
    v, e = map(int,sys.stdin.readline().split(" "))
    graph = [[] for _ in range(v+1)]
    visited = [0]*(v+1)
    con = True
    for j in range(e):
        a, b = map(int,sys.stdin.readline().split(" "))
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,v+1):
        if visited[i] == 0:
            if dfs(i,graph,visited,1) == False:
                con = False
                break
    if con == False:
        result.append("NO")
    else:
        result.append("YES")
for i in result:
    print(i)