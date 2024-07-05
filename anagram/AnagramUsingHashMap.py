def isanagram(string1, string2):
    hashmap = {}  # Empty directory

    for character in string1:
        if character not in hashmap:
            # add {character : value}
            hashmap[character] = 1
        else:
            # if character already in directory increment value by 1
            hashmap[character] += 1

    for character in string2:
        if character not in hashmap:
            # if character not in directory return False
            return False
        elif hashmap[character] == 1:
            # if character value is 1 del character
            del hashmap[character]
        else:
            # if character value is more than decrement value by 1
            hashmap[character] -= 1

    return not hashmap


if __name__ == '__main__':
    wordOne = input("Enter the first string: ")
    wordTwo = input("Enter the second string: ")
    # printing result
    print(isanagram(wordOne.lower(), wordTwo.lower()))
