def pow(n):
    if n==0:
        return 1
    return x*pow(n-1)
x=int(input())
n=int(input())
print(pow(n))