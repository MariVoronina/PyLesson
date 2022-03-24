new_f = open("moby_clean.txt", "r")
text = new_f.read().split("\n")
dict = {}
for i in set(text):
    dict[i] = text.count(i)
sortdict = {}
sorted_keys = sorted(dict, key=dict.get)
for i in sorted_keys:
    sortdict[i] = dict[i]
print("Первые пять самых редких слов: ", [i for i in list(sortdict.keys())[:5]])
print("Первые пять самых частых слов: ", [i for i in list(sortdict.keys())[-5:]])
new_f.close()
