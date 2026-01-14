import sys
from collections import deque
input = sys.stdin.readline
MAX = 100001

n, k = map(int, input().split())
arr = [-1] * MAX

if n>=k:
    print(n-k)
    sys.exit()

def bfs(start):
    q = deque([start])
    arr[start] = 0
   
    while q:
        cur_node = q.popleft()
        
        if cur_node == k:
            return arr[cur_node]

        for next_node in [cur_node*2,cur_node-1,cur_node+1]:
            
            if 0 <= next_node < MAX and arr[next_node] == -1:
                arr[next_node] = arr[cur_node] + 1
                q.append(next_node)

print(bfs(n))