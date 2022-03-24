import requests


f = requests.get("http://dfedorov.spb.ru/python3/src/romeo.txt")
trantab = str.maketrans({'.': None, ',': None, '-': " ", ';': None})
words = [i.lower() for i in f.text.translate(trantab).split()]
frequency = {}
ln = len(words)
for i in set(words):
    frequency[i] = round(words.count(i)/ln, 3)
print(frequency)
