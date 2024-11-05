"""
The list of numbers were given
which includes duplicates

job is to find the number which is only occur once
"""
def lonelyInteger(a):
    # checks length of list
    if len(a) == 2:
        # if both element in the list is same return no unique value
        if a[0] == a[1]:
            return "No lonely Integer"
    else:
        # sort a list
        a = sorted(a)
        # recursive
        if len(a) < 3:
            return a[0]
        elif a[0] != a[1]:
            return a[0]
        else:
            return lonelyInteger(a[2:])


# user input -> converting it to list of numbers -> calls function lonelyInteger to find lonelyInteger
# and print returned value
user_input = input('Enter a list of numbers separated by commas: ')
lists = list(map(int, user_input.split(',')))
print(lonelyInteger(lists))
