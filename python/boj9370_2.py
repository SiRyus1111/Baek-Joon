import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dist(start):
    dp = [INF] * (n+1)
    heap = []
    dp[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        cur_wei, cur_node = heapq.heappop(heap)
        
        if cur_wei > dp[cur_node]:
            continue

        for next_wei, next_node in graph[cur_node]:
            w = cur_wei + next_wei

            if w < dp[next_node]:
                dp[next_node] = w
                heapq.heappush(heap, (w, next_node))
    
    return dp


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    ans_node = []
    gh = INF
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d,b))
        graph[b].append((d,a))
        if (a == g and b == h) or (b == g and a == h):
            gh = min(gh, d)

    for _ in range(t):
        x = int(input())
        ans_node.append(x)

    dist_start = dist(s)
    dist_g = dist(g)
    dist_h = dist(h)
    
    ans = []

    for node in ans_node:
        path1 = dist_start[g] + gh + dist_h[node]
        path2 = dist_start[h] + gh + dist_g[node]
        shortest = dist_start[node]

        if (path1 == shortest and path1 < INF) or (path2 == shortest and path2 < INF):
            ans.append(node)
    ans.sort()
    print(*ans)