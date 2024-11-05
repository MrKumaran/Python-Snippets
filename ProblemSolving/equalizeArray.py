"""
EqualizeTheArray

To find the minimum elements to be deleted inorder
to get the remaining element in the array are equal

for instance
case 1:
Let array = [1, 3, 4, 4, 5, 6, 7, 8]

two elements are equal in array(4)

now need to find the minimum number of element to be deleted.
So, that remaining two element are 4's
In this case minimum number of element to be deleted is 6

case 2:
Let array = [1, 2, 3]

All elements are distinct. So, it's simple.
length of array - (length of array -1)
in other terms keep one element and delete remaining
In this case minimum number of element to be deleted is 2
"""

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
