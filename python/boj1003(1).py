memo = {0:(1,0),1:(0,1)}
def fibonacci(n):
    if n in memo:
        return memo[n]
    if n<0:
        return (0,0)
    z1,o1 = fibonacci(n-1)
    z2,o2 = fibonacci(n-2)
    memo[n] = (z1+z2,o1+o2)
    return memo[n]
t = int(input())
con = []
for i in range(t):
    a = int(input())
    con.append(fibonacci(a))
for z,o in con:
    print(z,o,sep=" ")