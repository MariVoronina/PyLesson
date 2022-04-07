import requests


f = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/opendata.stat")
lst = f.text.split("\n")
lst.pop(0)
lst2 = []
for i in lst:
    if "Количество заявок на потребительские кредиты" in i:
        if not("Россия" in i):
            lst2.append(i)
    else:
        break
lst3 = []
for i in lst2:
    lst3.append(i.split(","))
res = {}
for i in lst3:
    if "2017" in i[2] and i[1] in res.keys():
        res[i[1]] += int(i[3])
    elif "2017" in i[2] and not(i[1] in res.keys()):
        res[i[1]] = int(i[3])
mx = 0
res1 = 0
for i in res.keys():
    if res[i] >= mx:
        mx = res[i]
        res1 = i
print("Регион с максимальным количеством заявок на потребительские кредиты в 2017 году: ", res1)
