def fibonacci(n):
    if n == 0:
        return (1,0)
    elif n == 1:
        return (0,1)
    else:
        z1 ,o1 = fibonacci(n-2)
        z2 ,o2 = fibonacci(n-1)
        return (z1+z2,o1+o2)
a = int(input())
con = []
for i in range(a):
    num = int(input())
    con.append(fibonacci(num))
for z,o in con:
    print(z,o,sep=' ')