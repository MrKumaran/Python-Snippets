def isanagram(string1, string2):
    hashmap = {}

    for character in string1:
        if character in hashmap:
            hashmap[character] += 1
        else:
            hashmap[character] = 1

    for character in string2:
        if character not in hashmap:
            return False
        elif hashmap[character] == 1:
            del hashmap[character]
        else:
            hashmap[character] -= 1

    return not hashmap

if __name__ == '__main__':
    wordOne = input("Enter the first string: ")
    wordTwo = input("Enter the second string: ")
    print(isanagram(wordOne.lower(), wordTwo.lower()))
