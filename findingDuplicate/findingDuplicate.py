def isduplicate(array) -> bool:

    # converting list to a set because set removes duplicates
    setOfArray = set(array)

    # comparing length of list and set if len is not same then there is duplicate element
    if len(array) != len(setOfArray):
        return True
    else:
        return False


if __name__ == '__main__':
    user_input = input("Enter a array: ")
    # splitting the user input and converting it into int datatype then mapping finally making into list
    driverArray = list(map(int, user_input.split()))
    # prints result
    print(isduplicate(driverArray))
