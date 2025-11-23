from collections import deque
import sys
def bfs(graph,visited,start,end):
    visited[start] = 0
    q = deque([start])
    while q:
        k = q.popleft()
        for i in graph[k]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[k] + 1
        if i == end:
            break
    return visited[end]
n = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split(" "))
m = int(sys.stdin.readline())
visited = [-1]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(1, m+1):
    a, b = map(int,sys.stdin.readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)
print(bfs(graph,visited,start,end))

                    
