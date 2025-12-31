from collections import deque
import sys
def bfs(x,y,graph,n,m): #bfs
    q = deque([(x,y)]) #큐에 첫 값 넣기
    while q: #큐가 비면 종료
        x, y = q.popleft() #큐에서 값 꺼내기
        for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]: #상하좌우로 탐색
            fx = x+dx 
            fy = y+dy
            if 0<=fx<m and 0<=fy<n and graph[fy][fx]==1: #범위를 벗어나지 않았고 방문처리가 되어있지 않으면
                graph[fy][fx] = graph[y][x] + 1 #방문처리+값 기록
                q.append((fx,fy)) #큐에 새로운 값 넣기
    return graph[n-1][m-1] #도착지점에서의 거리 반환
n, m = map(int, sys.stdin.readline().split(" "))
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
print(bfs(0,0,graph,n,m))