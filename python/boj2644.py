from collections import deque
import sys
def bfs(graph,visited,start,end): #BFS
    visited[start] = 0 #시작 노드 방문 처리
    q = deque([start]) #큐에 시작 노드 삽입
    while q: #큐가 비면 종료
        k = q.popleft() #큐에서 가장 먼저 들어온 값 뺴내서 k에 저장
        if k == end: #만약 도착노드가 현재노드면
            return visited[k] #현재노드의 값 반환
        for i in graph[k]: #그래프 탐색
            if visited[i] == -1: #방문하지 않았으면
                q.append(i) #큐에 현재 노드 추가
                visited[i] = visited[k] + 1 #현재 노드 방문 처리
    return -1 #도착노드에 도착하지 못했으면 -1 반환
n = int(sys.stdin.readline()) #노드 수(사람 수)
start, end = map(int, sys.stdin.readline().split(" ")) #시작지점과 도착지점(촌수를 계산해야하는 사람들의 번호)
m = int(sys.stdin.readline()) #간선 갯수(부모와 자식간의 관계 개수)
visited = [-1]*(n+1) #방문 처리할 배열
graph = [[] for _ in range(n+1)] #그래프
for i in range(1, m+1): #그래프에 입력받기
    a, b = map(int,sys.stdin.readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)
print(bfs(graph,visited,start,end)) #bfs실행한 반환값을 출력