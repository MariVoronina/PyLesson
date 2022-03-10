students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня": 10}

good = []
bad = []
for i in grades:
    if grades.get(i) >= 8:
        good.append(i)
    else:
        bad.append(i)
print(good)
print(bad)
