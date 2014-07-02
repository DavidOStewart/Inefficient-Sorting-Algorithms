import random

def stoogesort(n,i,j):
    if n[j]<n[i]:
        n[i] ^= n[j]
        n[j] ^= n[i]
        n[i] ^= n[j]
    if (j-i+1) >= 3:
        t = int((j - i + 1) / 3)
        stoogesort(n,i,j-t)
        stoogesort(n,i+t,j)
        stoogesort(n,i,j-t)
    return n

a=[]
for x in range(10):
    a.append(random.randint(0,100))

print(stoogesort(a,0,9))
