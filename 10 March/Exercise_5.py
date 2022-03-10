marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}

n = int(input("Введите оценку от 1 до 10: "))
k = 0
for i in marks:
    k += sum(1 if j >= n else 0 for j in marks[i])
print("Количество оценок больше заданной: ", k)
