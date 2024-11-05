def bigSorting(unsorted):
    numArray = list(map(int, unsorted))
    numArray.sort()
    strArray = list(map(str, numArray))
    return strArray


unsorted = ['6', '31415926535897932384626433832795', '1', '3', '10', '3', '5']
result = bigSorting(unsorted)
print(result)