n = input("Введите обратную польскую запись: ")


def calc(zap: str):
    stek = []
    pol = list(zap)
    for i in pol:
        if i == "+":
            if len(stek) >= 2:
                s = stek.pop()
                s1 = stek.pop()
                stek.append(s+s1)
            else:
                return ("Неправильная польская запись")
        elif i == "-":
            if len(stek) >= 2:
                s = stek.pop()
                s1 = stek.pop()
                stek.append(s1-s)
            else:
                return ("Неправильная польская запись")
        elif i == "*":
            if len(stek) >= 2:
                s = stek.pop()
                s1 = stek.pop()
                stek.append(s*s1)
            else:
                return ("Неправильная польская запись")
        elif i == "/":
            if len(stek) >= 2:
                s = stek.pop()
                s1 = stek.pop()
                stek.append(s1//s)
            else:
                return ("Неправильная польская запись")
        else:
            stek.append(int(i))
    if len(stek) > 1:
        return ("Неправильная польская запись")
    return stek[0]


print(calc(n))
