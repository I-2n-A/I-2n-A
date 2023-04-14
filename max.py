import math

n = int(input())
spisok = []
for i in range(n):
    spisok.insert(i, input())
sum=0
for i in range(n):
    if spisok[i]<max(spisok):
        sum=sum+float(spisok[i])
    else: break
print(sum)
