import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

T = int(input())

def dist(start_node):
    dp = [INF] * (node_num + 1)
    heap = []
    dp[start_node] = 0
    heapq.heappush(heap,(0,start_node))
    
    while heap:
        cur_weight, cur_node = heapq.heappop(heap)

        if dp[cur_node] < cur_weight:
            continue
        
        for next_weight, next_node in graph[cur_node]:
            w = cur_weight + next_weight
            
            if dp[next_node] > w:
                dp[next_node] = w
                heapq.heappush(heap, (w, next_node))
    return dp

for i in range(T):
    node_num, edge_num, ans_node_num = map(int, input().split())
    start_node, es_node_1, es_node_2 = map(int, input().split())
    
    hg = INF
    graph = [[] for _ in range(node_num + 1)]
    for _ in range(edge_num):
        a, b, d = map(int, input().split())
        graph[a].append((d,b))
        graph[b].append((d,a))
        if (a == es_node_1 and b == es_node_2) or (b == es_node_1 and a == es_node_2):
            hg = min(d, hg)

    ans_node = [int(input()) for _ in range(ans_node_num)]
    
    start_node_dp = dist(start_node)
    es_node_1_dp = dist(es_node_1)
    es_node_2_dp = dist(es_node_2)

    a1 = start_node_dp[es_node_1]
    b1 = start_node_dp[es_node_2]

    A = a1 + hg
    B = b1 + hg
    
    ans = []
    for node in ans_node:
        
        path1 = start_node_dp[es_node_1] + hg + es_node_2_dp[node]
        path2 = start_node_dp[es_node_2] + hg + es_node_1_dp[node]


        if path1 == start_node_dp[node] or path2 == start_node_dp[node]:
            if start_node_dp[node] != INF:
                ans.append(node)

    ans.sort()
    print(*ans)