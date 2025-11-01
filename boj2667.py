count = 0
graph = []
cnt = []
result = 0
n = int(input())
for i in range(n):
    graph.append(list(map(int,input())))
def dfs(x,y,graph):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        global count
        count+=1
        dfs(x+1,y,graph)
        dfs(x-1,y,graph)
        dfs(x,y+1,graph)
        dfs(x,y-1,graph)
        return True
    return False
for i in range(n):
    for j in range(n):
        if dfs(i,j,graph) == True:
            cnt.append(count)
            result += 1
            count = 0
cnt.sort()
print(result)
for i in cnt:
    print(i)