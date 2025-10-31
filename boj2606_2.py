def virus(graph,v,visited):
    visited[v] = True
    count = 1
    for i in graph[v]:
        if not visited[i]:
            count += virus(graph,i,visited)
    return count
com = int(input())
net = int(input())
graph = [[] for _ in range(com+1)]
visited = [False]*(com+1)
for i in range(net):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(virus(graph,1,visited))
