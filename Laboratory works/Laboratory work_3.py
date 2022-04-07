import json

fl = open("todo list.json", "w+")
fl.close()

res = []

while True:
    k = input("Введите команду из предложенных:\n1 - Добавить задачу\n2 - Вывести список задач\n3 - Выход\nВаша команда: ")
    if k == "1":
        z = input("\nСформулируйте задачу: ")
        c = input("Добавьте категорию к задаче: ")
        t = input("Добавьте время к задаче: ")
        print("\n")
        res.append({"category": c, "name": z, "time": t})
        fl = open("todo list.json", "w")
        fl.write(json.dumps(res))
        fl.close()
    elif k == "2":
        fl = open("todo list.json", "r")
        lst = json.load(fl)
        fl.close()
        print("\n")
        for i in lst:
            print("Задача: ", i["name"], "  Категория: ", i["category"], "  Дата: ", i["time"])
        print("\n")
    elif k == "3":
        break
    else:
        print("Неправильно введённая команда")
