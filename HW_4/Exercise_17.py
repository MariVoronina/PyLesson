import random
import statistics


lst = [random.randint(-100000, 100000) for _ in range(8)]
print(lst)
mn = min(lst)
mx = max(lst)
print("Максимальный элемент: ", mx)
print("Минимальный элемент: ", mn)
imx = lst.index(mx)
imn = lst.index(mn)
if imn < imx:
    if len(lst[imn+1:imx]) != 0:
        print("Среднее арифметическое: ", sum(lst[imn+1:imx])/len(lst[imn+1:imx]))
    else:
        print("Числа отсутствуют")
else:
    print("Медиана: ", statistics.median(lst[imx+1:imn]))
