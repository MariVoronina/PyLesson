marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}
categories = {'отлично' : [8, 9, 10],
             'хорошо' : [6, 7],
             'удовлетворительно' : [4, 5],
             'неуд' : [0, 1, 2, 3]}

mean = []
for i in range(8):
    s = sum(marks[j][i] for j in marks)
    k = sum(1 for j in marks)
    mean.append(round(s/k))
n = int(input("Введите номер курса от 1 до 8: "))
for i in categories:
    if mean[n-1] in categories[i]:
        print("Курс ", n, " - ")
