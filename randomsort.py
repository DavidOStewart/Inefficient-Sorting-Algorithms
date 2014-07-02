import random

def randomsort():
    a = []
    for x in range(10):
        a.append(random.randint(1,100))
    print(a)
    while(a != sorted(a)):
        rand1 = random.randint(0,9)
        rand2 = random.randint(0,9)
        a[rand1] = a[rand1] ^ a[rand2]
        a[rand2] = a[rand2] ^ a[rand1]
        a[rand1] = a[rand1] ^ a[rand2]
    return a

print(randomsort())
