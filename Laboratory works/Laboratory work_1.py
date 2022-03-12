documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}


def p(n: str):
    for i in documents:
        if i['number'] == n:
            return i['name']
    return None


def s(n: str):
    for i in directories:
        if n in directories[i]:
            return i
    return None


def l():
    st = ""
    for i in documents:
       st = st + f"№: {i['number']}, тип: {i['type']}, владелец: {i['name']}, полка хранения: {s(i['number'])}\n"
    return st


def ads(n: str) -> bool:
    if n in list(directories.keys()):
        return False
    else:
        directories[n] = []
        return True


def ds(n: str):
    if n in list(directories.keys()) and directories[n] == []:
        del directories[n]
        return "1"
    elif n in list(directories.keys()):
        return "2"
    else:
        return "3"


def ad(n: str, t: str, v: str, d: str) -> bool:
    if d in list(directories.keys()):
        documents.append({'type': t, 'number': n, 'name': v})
        directories[d].append(n)
        return True
    return False


def d(n: str) -> bool:
    for i in documents:
        if i['number'] == n:
            documents.remove(i)
            return True
    return False


def m(n: str, dr: str):
    for i in documents:
        if i['number'] == n and dr in list(directories.keys()):
            for j in list(directories.keys()):
                if n in directories[j]:
                    directories[j].remove(n)
                    directories[dr].append(n)
                    return "1"
        elif i['number'] == n and not dr in list(directories.keys()):
            return "2"
    return "3"


while True:
    k = input("Введите команду: ")
    if k == "q":
        break
    if k == "p":
        m = input("Введите номер документа: ")
        if p(m) != None:
            print("Владелец документа: ", p(m))
        else:
            print("Документ не найден в базе")
        continue
    if k == "s":
        m = input("Введите номер документа: ")
        if s(m) != None:
            print("Документ хранится на полке: ", s(m))
        else:
            print("Документ не найден в базе")
        continue
    if k == "l":
        print(l())
        continue
    if k == "ads":
        m = input("Введите номер полки: ")
        if ads(m):
            print("Полка добавлена. Текущий перечень полок: ", list(directories.keys()))
        else:
            print("Такая полка уже существует. Текущий перечень полок: ", list(directories.keys()))
        continue
    if k == "ds":
        m = input("Введите номер полки: ")
        if ds(m) == "1":
            print("Полка удалена. Текущий перечень полок: ", list(directories.keys()))
        elif ds(m) == "2":
            print("На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: ", list(directories.keys()))
        else:
            print("Такой полки не существует. Текущий перечень полок: ", list(directories.keys()))
        continue
    if k == "ad":
        num = input("Введите номер докуметна: ")
        tu = input("Введите тип докуметна: ")
        vl = input("Введите владельца докуметна: ")
        dir = input("Введите полку для хранения: ")
        if ad(num, tu, vl, dir):
            print("Документ добавлен. Текущий список документов:")
            print(l())
        else:
            print("Такой полки не существует. Добавьте полку командой ads.\nТекущий спиоск документов:")
            print(l())
        continue
    if k == "d":
        m = input("Введите номер документа: ")
        if d(m):
            print("Документ удалён.\nТекущий список документов:")
            print(l())
        else:
            print("Документ не найден в базе.\nТекущий список документов:")
            print(l())
        continue
    if k == "m":
        num = input("Введите номер документа: ")
        direct = input("Введите номер полки: ")
        if m(num, direct) == "1":
            print("Документ перемещён.\nТекущий спискок документов:")
            print(l())
        elif m(num, direct) == "2":
            print("Такой полки не существует. Текущий перечень полок: ", list(directories.keys()))
        else:
            print("Документ не найден в базе.\nТекущий список документов:")
            print(l())
        continue   
    print("Нераспознаваемая команда")
