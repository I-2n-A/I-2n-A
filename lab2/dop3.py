def Summ(x):
    a = x
    s = 0
    while a > 0:
        s += a % 10 
        a //= 10 
    return s
n=int(input())
s=int(input())
print(s==Summ(n))
