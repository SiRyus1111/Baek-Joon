from collections import deque
import sys
def virus(graph,start,visited):
    visited[start] = True
    q = deque([start])
    count = 0
    while q:
        n = q.popleft()
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                count+=1
    return count
k = int(sys.stdin.readline().strip())
l = int(sys.stdin.readline().strip())
graph = [[] for _ in range(k+1)]
for i in range(l):
    n, j = map(int, input().split(" "))
    graph[n].append(j)
    graph[j].append(n)
for i in range(1,k+1):
    graph[i].sort()
visited = [False]*(k+1)
count = 0
print(virus(graph,1,visited))