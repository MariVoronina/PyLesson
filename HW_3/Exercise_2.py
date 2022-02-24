import random

def password():
    l = random.randint(7,10)
    lst = []
    lst_1 = []
    for i in range(33,127):
        lst.append(chr(i))
    for i in range(l):
        lst_1.append(random.choice(lst))
    return ''.join(lst_1)
