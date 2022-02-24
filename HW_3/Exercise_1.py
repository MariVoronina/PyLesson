import random

n = random.randint(1,10)
while True:
    c = int(input("Введите число от 1 до 10: "))
    if n == c:
        print("Вы угадали!")
        break
    else:
        if c > n:
            print("Введённое число больше загаданного! Попробуйте еще раз")
        else:
            print("Введённое число меньше загаданного! Попробуйте еще раз")
