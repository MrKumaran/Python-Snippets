min_limit = 1  # Static
no_of_numbers = 3  # Static
max_total = int(input("max_total:"))
max_limit = int(input("max_limit:"))

result = []
allPossibleList = []
for i in range(min_limit, max_limit+1):
    for j in range(min_limit, max_limit+1):
        for k in range(min_limit, max_limit+1):
            allPossibleList.append([i, j, k])
for i in allPossibleList:
    if sum(i) == max_total:
        result.append(i)
print(result)
