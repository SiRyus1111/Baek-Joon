import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
picture = []
visited_a = [[0] * n for _ in range(n)]
count_a = 0
visited_b = [[0] * n for _ in range(n)]
count_b = 0
moves = [[1,0],[-1,0],[0,1],[0,-1]]
for i in range(n):
    arr = list(input().rstrip())
    picture.append(arr)
def bfs(y,x,visited):
    visited[y][x] = 1
    q = deque([(y,x)])
    key = picture[y][x]
    while q:
        y, x = q.popleft()
        for dy, dx in moves:
            ky = dy + y
            kx = dx + x
            if 0<=kx<n and 0<=ky<n and visited[ky][kx] == 0 and picture[ky][kx] == key:
                visited[ky][kx] = 1
                q.append((ky,kx))
for y in range(n):
    for x in range(n):
        if visited_a[y][x] == 0:
            bfs(y,x,visited_a)
            count_a += 1
for y in range(n):
    for x in range(n):
        if picture[y][x] == "G":
            picture[y][x] = "R"
for y in range(n):
    for x in range(n):
        if visited_b[y][x] == 0:
            bfs(y,x,visited_b)
            count_b += 1
print(count_a,count_b,sep=" ")