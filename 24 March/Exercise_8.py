import requests


f = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/text.txt")
trantab = str.maketrans({'.': None, ',': None, '-': " ", ';': None})
words = [i for i in f.text.translate(trantab).split()]
print(words)
k_upper = sum([1 if "A"<= i[0] <= "Z" else 0 for i in words])
k_digits = sum([len(i) if i.isdigit() else 0 for i in words])
k_probels = sum([1 if i == " " else 0 for i in list(f.text)])
print("Количество букв в верхнем регистре: ", k_upper)
print("Количество цифр: ", k_digits)
print("Количество пробелов: ", k_probels)
