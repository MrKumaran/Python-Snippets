def isanagram(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        return sorted(str1) == sorted(str2)

if __name__ == '__main__':
    word1 = input("Enter the first string: ")
    word2 = input("Enter the second string: ")
    print(isanagram(word1.lower(), word2.lower()))
