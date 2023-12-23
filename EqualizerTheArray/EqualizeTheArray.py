def equalizeArray(array):
    """
    convert array to set to remove duplicates
    find max of set with key value array.Count
    and count the value from max in array and
    subtract that value count from length of that array.
    ------------------------------------------------------------------------------
    max(set(array), key=array.count returns maximum number of times a number occurs in 
    list it doesn't check for maximum value rather it checks for number of time a element repeated
    """
    return len(array) - array.count(max(set(array), key=array.count))


if __name__ == '__main__':

    # Getting input and mapping into arr
    arr = list(map(int, (input("Enter a List of numbers seperated by Space: ").rstrip().split())))

    # calling equalizeArray function with array as argument
    result = equalizeArray(arr)

    # print result at last
    print(result)
