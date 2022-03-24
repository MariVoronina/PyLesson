import requests


f1 = requests.get("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/moby.txt")
f2 = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/text.txt")
trantab = str.maketrans({'.': None, ',': None, '-': " ", ';': None})
lst1 = [i.lower() for i in f1.text.translate(trantab).split()]
lst2 = [i.lower() for i in f2.text.translate(trantab).split()]
print("Количество уникальных слов в первом файле: ", len(set(lst1)))
print("Количество уникальных слов во втором файле: ", len(set(lst2)))
k = sum([1 if i in lst2 else 0 for i in lst1])
print("Количество общих слов: ", k)
