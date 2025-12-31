import sys
sys.setrecursionlimit(10**6)
def dfs(v,graph,visited,color): #DFS
    visited[v] = color #현재 노드 방문 처리
    for i in graph[v]: #그래프 탐색
        if visited[i] == 0: #방문하지 않았고
            if not dfs(i,graph,visited,-color): #False를 반환하지 않았으면 DFS재귀호출
                return False
        elif visited[i] == visited[v]: #같은 색이 연속되면
            return False #False 반환
    return True #잘못되지 않았으면 True 반환
t = int(sys.stdin.readline().rstrip()) #테스트 케이스 수
result = [] #결과를 저장할 배열
for i in range(t):
    v, e = map(int,sys.stdin.readline().split(" ")) #정점과 간선 갯수
    graph = [[] for _ in range(v+1)] #그래프
    visited = [0]*(v+1) #방문 처리할 배열
    con = True #이분 그래프 체크
    for j in range(e): #간선 입력 받기
        a, b = map(int,sys.stdin.readline().split(" "))
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,v+1): #한 정점씩
        if visited[i] == 0: #방문하지 않았으면
            if dfs(i,graph,visited,1) == False: #DFS후 False를 반환했으면
                con = False #체크
                break #for문 탈출
    if con == False: #배열에 이분 그래프 여부 저장
        result.append("NO")
    else:
        result.append("YES")
for i in result: #출력
    print(i)