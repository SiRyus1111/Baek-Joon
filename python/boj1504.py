import heapq
import sys
input = sys.stdin.readline
INF = int((1e10))

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

v1, v2 = map(int, input().split())

def dijkstra(start,end):
    heap = []
    dp = [INF] * (n+1)
    dp[start] = 0
    heapq.heappush(heap, (0,start))
    while heap:
        weight, cur_node = heapq.heappop(heap)

        if dp[cur_node] < weight:
            continue

        for next_weight, next_node in graph[cur_node]:
            w = weight + next_weight
            if dp[next_node] > w:
                dp[next_node] = w
                heapq.heappush(heap, (w, next_node))
    return dp[end]

a1 = dijkstra(1, v1)
b1 = dijkstra(1, v2)
a2 = dijkstra(v1, v2)
b2 = dijkstra(v2, v1)
a3 = dijkstra(v2, n)
b3 = dijkstra(v1, n)
a_sum = a1 + a2 + a3
b_sum = b1 + b2 + b3

ans = min(a_sum,b_sum)
print(-1 if ans >= INF else ans)