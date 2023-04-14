a=int(input())
def divs(n):
   k=0
   for i in range(2,n):
      if (n%i==0):
         k=k+1
   return k
print(divs(a))

    