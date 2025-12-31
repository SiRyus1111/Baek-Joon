from collections import deque
def dfs(arr,v,visited,result):
    visited[v] = True
    result.append(v)
    for i in arr[v]:
        if not visited[i]:
            dfs(arr,i,visited,result)
def bfs(arr,v,visited,result):
    visited[v] = True
    q = deque([v])
    while q:
        k = q.popleft()
        result.append(k)
        for i in arr[k]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
n, m, v = map(int,input().split())
result1 = []
result2 = []
visited1 = [False]*(n+1)
visited2 = [False]*(n+1)
arr = [[] for _ in range(n+1)]
for i in range(m):
    num, k = map(int, input().split())
    arr[num].append(k)
    arr[k].append(num)
for i in range(1,n+1):
    arr[i].sort()
dfs(arr,v,visited1,result1)
bfs(arr,v,visited2,result2)
for i in result1:
    print(i,end=" ")
print()
for i in result2:
    print(i,end=" ")

