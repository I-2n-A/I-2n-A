import math

n = int(input())
spisok = []
pr = 1
for i in range(n):
    spisok.insert(i, input())
for i in range(n):
    k = float(spisok[i])
    if k<0: pr=pr*k
print(pr)
