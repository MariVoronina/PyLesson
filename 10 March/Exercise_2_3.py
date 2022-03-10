good = []
bad = []
for i in grades:
    if grades.get(i) >= 8:
        good.append(i)
    else:
        bad.append(i)
print(good)
print(bad)
