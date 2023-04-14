
x=int(input())
n=int(input())
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)    
def f(n):
    if n==0:
        return 1
    return x*f(n-1)
print(round(f(n)/fact(n),3))

