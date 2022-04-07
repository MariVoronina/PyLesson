import os


def numbers(orig_name: str, new_name: str):
    if os.path.exists(orig_name):
        fl = open(orig_name, "r")
        text = fl.read().split("\n")
        fl.close()
        res = []
        n = 1
        for i in text:
            res.append(f"{n} {i}")
            n += 1
        fl1 = open(new_name, "w+")
        fl1.write("\n".join(res))
        fl1.close
        return "Файл обработан"
    else:
        return "Файла не существует"
