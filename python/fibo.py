import sys
sys.setrecursionlimit(10**6)
def fibo(n):
    global cnt
    cnt += 1
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibo(n-1) + fibo(n-2)
cnt = 0
n = fibo(40)
print(cnt)