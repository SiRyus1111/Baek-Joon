from collections import deque
import sys
def bfs(start,graph,visited):#BFS
    q = deque([start])#시작 노드 큐에 삽입
    visited[start] = 1 #시작 노드 그룹(색) 지정
    while q: #큐가 비면 종료
        m = q.popleft() 
        for i in graph[m]:
            if visited[i] == 0: #방문하지 않았으면
                visited[i] = -visited[m] #다른 그룹(색) 지정
                q.append(i) #큐에 노드 삽입
            elif visited[i] == visited[m]: #만약 같은 그룹이 연속된다면(이분 그래프가 아니라면)
                return False #False 반환
    return True #문제가 없으면(이분 그래프라면) True 반환
k = int(sys.stdin.readline().rstrip()) #테스트 케이스 수
result = [] #결과를 모아서 저장할 배열
for i in range(k):
    v, e = map(int,sys.stdin.readline().split()) #정점의 갯수와 간선의 갯수
    visited = [0]*(v+1) #방문 처리할 배열
    graph = [[] for _ in range(v+1)] #그래프
    con = True #이분 그래프 여부 저장할 변수
    for i in range(e): #간선의 갯수만큼 입력받기
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,v+1): #첫 노드부터 마지막 노드까지
        if visited[i] == 0: #그 노드를 방문하지 않았다면 BFS 실행
            if bfs(i,graph,visited) == False: #BFS결과가 False라면(이분 그래프가 아니라면)
                con = False #변수 = False
                break #for문 탈출
    if con == False: #con값에 따라 배열에 결과 추가
        result.append("NO")
    else:
        result.append("YES")
for i in range(k): #한번에 출력
    print(result[i])