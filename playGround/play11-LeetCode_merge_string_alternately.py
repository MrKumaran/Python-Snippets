word1 = "abc"
word2 = "pqr"
word = []
pointer0 = 0
pointer1 = 0
length = len(word1) + len(word2)
for i in range(length):
    if pointer0 != len(word1):
        word.append(word1[pointer0])
        pointer0 += 1
    if pointer1 != len(word2):
        word.append(word2[pointer1])
        pointer1 += 1
print("".join(word))