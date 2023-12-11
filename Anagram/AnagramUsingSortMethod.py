def isanagram(str1, str2):  # check for anagram or not
    if len(str1) != len(str2):
        # if length of strings are not same then automatically it is not anagram
        return False
    else:
        # sorting the string and comparing two strings
        return sorted(str1) == sorted(str2)

if __name__ == '__main__':
    word1 = input("Enter the first string: ")
    word2 = input("Enter the second string: ")
    # printing the result
    print(isanagram(word1.lower(), word2.lower()))
