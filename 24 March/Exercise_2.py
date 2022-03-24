import requests
import statistics
import matplotlib.pyplot as plt

f = requests.get("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat")
lst = [float(i) for i in f.text.split("\n") if i != '']
print("Максимальная температура: ", max(lst))
print("Минимальная температура: ", min(lst))
print("Средняя температура: ", statistics.mean(lst))
print("Количество уникальных температур: ", len(set(lst)))

coord = [i for i in range(1, len(lst)+1)]
plt.plot(coord, lst)
plt.show()
