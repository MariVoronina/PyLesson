import requests


f = requests.get("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/moby.txt")
trantab = str.maketrans({'.': None, ',': None, '-': " ", ';': None })
lst = "\n".join([i.lower() for i in f.text.translate(trantab).split()])

new_f = open("moby_clean.txt", "w+")
new_f.write(lst)
new_f.close()

new_f = open("moby_clean.txt", "r")
print(new_f.read())
new_f.close()
