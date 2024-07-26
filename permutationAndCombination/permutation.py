# permutation useful snippet
from itertools import permutations

characters = [13, 10, 9, 8, 13, 12, 18, 13]

perm = permutations(characters, 5)
l = []

for i in perm:
    l.append(list(i))

print(l)
for i in l:
    print(sum( i))