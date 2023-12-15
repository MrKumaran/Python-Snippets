string1 = input('Enter String 1: ')
string2 = input('Enter String 2: ')

zip_string = zip(string1, string2)
enum_string = enumerate(zip_string)
for i, (a,b) in enum_string:
    if a != b:
        print(f'Unmatched Index: {i}')

