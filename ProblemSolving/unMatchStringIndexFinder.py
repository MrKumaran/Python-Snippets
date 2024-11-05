"""
Gets two strings (or array of number if modifications made)
return index at where two strings are different
"""

# Getting Two string from user
string1 = input('Enter String 1: ')
string2 = input('Enter String 2: ')
# zipping each character from string1 and string 2 together
zip_string = zip(string1, string2)
# enumerating zip_string list with index for each list
enum_string = enumerate(zip_string)
# taking each element in enum_string and evaluating it
for i, (a, b) in enum_string:
    # check not equal element and print it indexes
    if a != b:
        print(f'Unmatched Index: {i}')
