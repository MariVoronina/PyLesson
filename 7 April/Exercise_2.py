n = input("Введите последовательность символов-ограничителей: ")


def check_delimiter(zap: str):
    stek = []
    sim = list(zap)
    for i in sim:
        if i == "(":
            stek.append(i)
        elif i == "{":
            stek.append(i)
        elif i == "[":
            stek.append(i)
        elif i == "]":
            if stek.count("[") > 0:
                stek.pop(stek.index("["))
            else:
                return False
        elif i == "}":
            if stek.count("{") > 0:
                stek.pop(stek.index("{"))
            else:
                return False
        elif i == ")":
            if stek.count("(") > 0:
                stek.pop(stek.index("("))
            else:
                return False
    if len(stek) > 0:
        return False
    return True


print(check_delimiter(n))
