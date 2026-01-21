import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    stock_sum = 0
    stock_max = stock[n-1]
    
    for j in range(n-1, -1, -1):
        
        if stock_max > stock[j]:
            stock_sum += stock_max - stock[j]
        
        else:
            stock_max = stock[j]
    
    print(stock_sum)