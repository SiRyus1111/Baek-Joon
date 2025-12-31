import sys
def dfs(start,graph,visited): #큐 기반 BFS와 같은 구조(DFS)
    visited[start] = 1 #시작 노드 그룹 지정
    st = [start] #시작 노드 스택(배열)에 삽입
    while st: #스택이 비면 종료
        s = st.pop() #스택에서 가장 마지막에 들어온 값 꺼내서 저장
        for i in graph[s]: #그래프 탐색
            if visited[i] == 0: #방문하지 않았으면
                visited[i] = visited[s]*-1 #다른 그룹 지정
                st.append(i) #스택에 노드 삽입
            elif visited[i] == visited[s]: #같은 그룹이 연속된다면
                return False #False 반환
    return True #문제 없으면 True 반환
t = int(sys.stdin.readline()) #테스트 케이스 수
result = [] #결과를 저장할 배열
for i in range(t):
    v, e = map(int,sys.stdin.readline().split(" ")) #정점과 간선의 갯수
    graph = [[] for _ in range(v+1)] #그래프
    visited = [0]*(v+1) #방문 처리할 배열
    con = True #이분 그래프 여부
    for i in range(e): #간선 입력받아 그래프에 저장
        u, k = map(int,sys.stdin.readline().split(" "))
        graph[u].append(k)
        graph[k].append(u)
    for i in range(1,v+1):#1번 노드부터 마지막 노드까지 탐색
        if visited[i] == 0: #방문하지 않았다면
            if dfs(i,graph,visited) == False: #dfs실행후 False값이면(이분 그래프가 아니라면)
                con = False #변수에 False저장
                result.append("NO") #결과를 저장할 배열에 NO저장
                break #반복문 탈출
    if con: #이분 그래프라면
        result.append("YES") #YES저장
for i in result: #출력
    print(i)