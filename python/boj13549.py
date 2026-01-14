import sys
import heapq
input = sys.stdin.readline
max_value = 100001
INF = sys.maxsize

n, k = map(int, input().split())

if n >= k:
    print(n-k)
    sys.exit()

dp = [INF] * max_value

def dist(start,end):
    dp[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        cur_sec, cur_node = heapq.heappop(heap)

        if dp[cur_node] < cur_sec:
            continue

        if cur_node == end:
            return cur_sec

        for next_sec, next_node in [(0, cur_node * 2), (1, cur_node + 1), (1, cur_node - 1)]:
            sec = cur_sec + next_sec

            if 0 <= next_node < max_value and dp[next_node] > sec:
                dp[next_node] = sec
                heapq.heappush(heap, (sec, next_node))

print(dist(n,k))