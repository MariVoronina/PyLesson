try:
    n = int(input("Введите первое число: "))
    m = int(input("Введите второе число: "))
    op = input("Введите операцию: +, -, /: ")
    if op == "+":
        print(n+m)
    elif op == "-":
        print(n-m)
    elif op == "/":
        try:
            print(n/m)
        except ZeroDivisionError:
            print("Ошибка деления на ноль")
    else:
        print("Неправильно введена операция")
except ValueError:
    print("Ошибка преобразования типов")
