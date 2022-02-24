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

def protect_password(s: str):
    if len(s) < 8:
        return False
    else:
        count_int = 0
        count_title = 0
        count_lower = 0
        for i in s:
            if '0' <= i <= '9':
                count_int += 1
            elif 'A' <= i <= 'Z':
                count_title += 1
            elif 'a' <= i <= 'z':
                count_lower += 1
        if count_title >= 1 and count_lower >= 1 and count_int >= 1:
            return True
        else:
            return False

kol_pop = 1
pas = password()
while not(protect_password(pas)):
    kol_pop += 1
    pas = password()
print("Количество попыток: ", kol_pop)
print("Правильный пароль: ",pas)
