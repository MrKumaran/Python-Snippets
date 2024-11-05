n = 8
k = 5
contests = [[13, 1], [10, 1], [9, 1], [8, 1], [13, 1], [12, 1], [18, 1], [13, 1]]
importantContest = []
notImportantContest = []
for i in contests:
    if i[1] == 1:
        importantContest.append(i[0])
    else:
        notImportantContest.append(i[0])
luck = sum(notImportantContest)
win = 0
for _ in range(len(importantContest)-k):
    win += min(importantContest)
    importantContest.remove(min(importantContest))
luck = luck + sum(importantContest) - win
print(luck)