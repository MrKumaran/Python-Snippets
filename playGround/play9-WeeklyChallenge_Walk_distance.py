calorie = [5, 10, 7]
walk_distance = 0

for c in range(len(calorie)):
    m = max(calorie)
    calorie.remove(m)
    walk_distance = walk_distance + ((2**c)*m)

print(walk_distance)