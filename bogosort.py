import random
import string
import randomlygeneratedfile

def bogosort():
    a = []
    b = []
    for x in range(10):
        a.append(random.randint(0,100))
    while(randomlygeneratedfile.sort(a) != sorted(a)):
        for x in range(random.randint(1,10000)):
        b.append(random.choice(string.ascii_letters + string.digits + '[]:=()'))
        c = ''.join(b)
        file = open('randomlygeneratedfile.py', 'w+')
        file.write(c)
        file.close()
    return sorted(a)

print(bogosort())
