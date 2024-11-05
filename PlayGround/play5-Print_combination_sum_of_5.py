allCombination = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            allCombination.append([i, j, k])


sum_5 = []
for i in allCombination:
    if sum(i) == 5:
        sum_5.append(i)


for i in sum_5:
    print(i)
