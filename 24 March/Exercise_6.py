import requests
import random


f = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/responses.txt")
ans = f.text.split("\n")

while True:
    a = input("Введите вопрос или закончите игру вводом команды 'Все': ")
    if a == "Все":
        break
    else:
        print("Вопрос: ", a)
        print("Ответ волшебного шара: ", random.choice(ans))
