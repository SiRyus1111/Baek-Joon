import sys
import heapq
input = sys.stdin.readline

heap = []
v, e = map(int, input().split())
dp = [[1e9] * (v+1) for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
    dp[a][b] = c
    heapq.heappush(heap, (c, a, b))

while heap:
    cur_wei, start_node, cur_node = heapq.heappop(heap)

    if start_node == cur_node:
        print(cur_wei)
        sys.exit()
    
    if cur_wei > dp[start_node][cur_node]:
        continue

    for next_wei, next_node in graph[cur_node]:
        w = cur_wei + next_wei
        if w < dp[start_node][next_node]:
            dp[start_node][next_node] = w
            heapq.heappush(heap, (w, start_node, next_node))
    
print(-1)