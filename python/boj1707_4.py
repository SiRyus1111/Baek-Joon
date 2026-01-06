import sys
from collections import deque
def bfs(start):
    if not visited[start] == 0:
        return True
    visited[start] = 1
    q = deque([start])
    while q:
        w = q.popleft()
        for nxt in graph[w]:
            if visited[nxt] == 0:
                visited[nxt] = -1 * visited[w]
                q.append(nxt)
            elif visited[nxt] == visited[w]:
                return False
            
    return True
input = sys.stdin.readline
k = int(input())
result = ["YES"] * k
for i in range(k):
    v, e = map(int, input().split(" "))
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        u, n = map(int, input().split(" "))
        graph[u].append(n)
        graph[n].append(u)
    for node in range(1,v+1):
        if not bfs(node):
            result[i] = "NO"
            break
for ans in result:
    print(ans)