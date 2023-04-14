def Check(x):
    a = x
    s = 0
    p = 1
    while a > 0:
        s += a % 10 
        a //= 10 
    if s != 1:
        while p < x:
            p *= s 
    return p == x
n=int(input()) 
for i in range(1, n+1):
    if Check(i):
        print(i,end=" ")