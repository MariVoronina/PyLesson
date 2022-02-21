import random

lst = input("Введите слова: ").split(' ')
slov = lst[random.randint(0,len(lst)-1)]
lst_new = list(slov)
n = random.randint(0,len(lst_new)-1)
b = lst_new[n]
lst_new[n] ="?"
print("Угадайте букву: " + ''.join(lst_new))
b_pol = input("Введите букву: ")
if b == b_pol:
    print("Победа")
else:
    print("Увы! Попробуте в другой раз!")
print("Слово: " + slov)
