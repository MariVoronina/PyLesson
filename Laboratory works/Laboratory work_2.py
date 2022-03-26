fl = open("students.txt", "w+")
fl.close()


def put(name: str, family_name: str):
    fl = open("students.txt", "r")
    lst = fl.read().split("\n")
    fl.close()
    fl = open("students.txt", "w")
    if lst == ['']:
        fl.write(f"{family_name} {name}")
    elif f"{family_name} {name}" in lst:
        print("Такой студент уже есть!")
    else:
        lst.append(f"{family_name} {name}")
        lst.sort()
        lst = "\n".join(lst)
        fl.write(lst)
    fl.close()


def find(family_name: str, name=None):
    fl = open("students.txt", "r")
    lst = fl.read().split("\n")
    fl.close()
    if name:
        for i in lst:
            if f"{family_name} {name}" in i:
                return "Студент есть"
        return "Такого студента нет"
    else:
        lst1 = []
        for i in lst:
            if family_name in i:
                lst1.append(i)
        if lst1:
            return lst1
        else:
            return "Таких студентов нет"


def replace(name: str, family_name: str, new_name=None, new_family_name=None):
    fl = open("students.txt", "r")
    lst = fl.read().split("\n")
    fl.close()
    if new_name and new_family_name is None:
        for i in lst:
            if f"{family_name} {name}" in i:
                remove(family_name, name)
                put(new_name, family_name)
                return "Имя изменено"
        return "Такого студента нет"
    elif new_family_name and new_name is None:
        for i in lst:
            if f"{family_name} {name}" in i:
                remove(family_name, name)
                put(name, new_family_name)
                return "Фамилия изменена"
        return "Такого студента нет"
    elif new_family_name and new_name:
        for i in lst:
            if f"{family_name} {name}" in i:
                remove(family_name, name)
                put(new_name, new_family_name)
                return "Имя и фамилия изменены"
        return "Такого студента нет"
    else:
        return "Вы не указали изменения"


def remove(family_name: str, name=None):
    fl = open("students.txt", "r")
    lst = fl.read().split("\n")
    fl.close()
    if name:
        for i in lst:
            if f"{family_name} {name}" in i:
                lst.remove(f"{family_name} {name}")
                lst = "\n".join(lst)
                fl = open("students.txt", "w+")
                fl.write(lst)
                fl.close()
                return "Студент удалён"
        return "Такого студента нет"
    else:
        lst1 = []
        for i in lst:
            if family_name in i:
                lst1.append(i)
        if lst1 is []:
            return "Такого студента нет"
        else:
            for i in lst1:
                lst.remove(i)
            lst = "\n".join(lst)
            fl = open("students.txt", "w+")
            fl.write(lst)
            fl.close()
            return "Студенты удалёны"


put("Мария", "Воронина")
put("Настя", "Воробьёва")
put("Юлия", "Александрова")
put("Александр", "Крестьянинов")
put("Денис", "Смолянинов")
put("Ваня", "Смолянинов")
print(find("Воронина", "Мария"))
print(find("Смолянинов"))
print(find("Бурин"))
print(replace("Мария", "Воронина", "Настя", "Веслеова"))
print(replace("Юлия", "Александрова", new_name="Настя"))
print(replace("Александр", "Крестьянинов", new_family_name="Попов"))
print(replace("Денис", "Смолянинов"))
print(replace("Костя", "Иванов"))
print(replace("Леша", "Орехов", new_name="Настя"))
print(replace("Вова", "Кравчук", new_family_name="Попов"))
print(remove("Смолянинов"))
print(remove("Попов", "Александр"))
print(remove("Воробьёва", "Саша"))

fl.close()
