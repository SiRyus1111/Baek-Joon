import sys
def dfs(start,graph,visited):
    visited[start] = 1
    st = [start]
    while st:
        s = st.pop()
        for i in graph[s]:
            if visited[i] == 0:
                visited[i] = visited[s]*-1
                st.append(i)
            elif visited[i] == visited[s]:
                return False
    return True
t = int(sys.stdin.readline())
result = []
for i in range(t):
    v, e = map(int,sys.stdin.readline().split(" "))
    graph = [[] for _ in range(v+1)]
    visited = [0]*(v+1)
    con = True
    for i in range(e):
        u, k = map(int,sys.stdin.readline().split(" "))
        graph[u].append(k)
        graph[k].append(u)
    for i in range(1,v+1):
        if visited[i] == 0:
            if dfs(i,graph,visited) == False:
                con = False
                result.append("NO")
                break
    if con:
        result.append("YES")
for i in result:
    print(i)