import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)
heap = []

v, e = map(int,input().split())
k = int(input())
dp = [inf] * (v+1)
graph = [[] for _ in range(v+1)]
for _ in range(e):
    node, next, w = map(int, input().split())
    graph[node].append((w,next))

def tlqkf(start):
    dp[start] = 0
    heapq.heappush(heap, (0,start))
    while heap:
        weight, cur_node = heapq.heappop(heap)

        if dp[cur_node] < weight:
            continue

        for next_weight, next_node in graph[cur_node]:
            w = weight + next_weight
            if w < dp[next_node]:
                dp[next_node] = w
                heapq.heappush(heap,(w, next_node))
tlqkf(k)
for i in range(1, v+1):
    print("INF" if dp[i] == inf else dp[i])