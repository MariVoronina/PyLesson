text = '''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''
lst = text.split("\n")
lst1 = [i.split() for i in lst]
lst2 = [[item[i] for i in range(len(item)) if len(item[i]) > 3] for item in lst1]
print(lst2)
