lst = [1, 5, 6.3, 6, None, 2.0, -4, None]
sr = sum([i if i != None else 0 for i in lst])/(len(lst) - sum([0 if i != None else 1 for i in lst]))
print([i if i != None else sr for i in lst])
