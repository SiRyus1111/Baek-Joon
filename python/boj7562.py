from collections import deque
import sys
move = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)] #움직임 미리 배열로 지정해놓기
def bfs(x,y,n,kx,ky): #bfs
    if x ==kx and y == ky: #시작지점과 도착지점이 같은경우
        return 0
    graph = [[-1]*n for _ in range(n)] #그래프 생성
    graph[y][x] = 0 #첫 시작지점 0으로 초기화
    q = deque([(x,y)]) #큐에 첫 시작지점 좌표 집어넣기
    while q: #큐가 비면 종료
        x,y = q.popleft() #큐에서 추출
        for fx, fy in move: #움직임 실행
            dx = x+fx
            dy = y+fy
            if 0<=dx<n and 0<=dy<n and graph[dy][dx]==-1: #밖으로 나가지 않았고, 방문하지 않았는지 체크
                graph[dy][dx] = graph[y][x]+1 #이동한 지점의 이동 횟수 저장
                if dy == ky and dx == kx: #도착했으면
                    return graph[dy][dx] #도착한 지점의 값을 반환
                q.append((dx,dy)) #큐에 좌표 추가
t = int(sys.stdin.readline().rstrip()) #테스트 케이스 수 입력받기
for i in range(t):
    n = int(sys.stdin.readline().rstrip()) #세로, 가로 길이
    x, y = map(int, sys.stdin.readline().split(" ")) #초기 위치
    kx, ky = map(int, sys.stdin.readline().split(" ")) #도착 위치
    print(bfs(x,y,n,kx,ky))