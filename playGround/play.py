# Play 1 - relational expression
"""
import re

# print('Hello'+'Ko')
lists = ["3", '', '#name', 'FirstName']
for I in lists:
    print(re.findall("\w+", i))
"""

# Play 2 - Time testing bw built-in count and for-if
"""import randomGenerator as r import time as t listOne = [22, 41, 39, 88, 100, 39, 58, 45, 87, 60, 92, 70, 92, 60, 18, 
51, 38, 42, 93, 69, 21, 8, 84, 37, 22, 63, 12, 81, 54, 63, 91, 54, 39, 37, 60, 39, 15, 35, 10, 69, 75, 94, 79, 49, 2, 
100, 49, 50, 67, 59, 8, 56, 60, 39, 6, 89, 1, 63, 29, 41, 80, 37, 33, 7, 45, 95, 72, 96, 91, 13, 61, 29, 44, 3, 94, 
56, 46, 24, 44, 33, 13, 1, 77, 70, 37, 60, 90, 7, 66, 66, 82, 98, 56, 39, 12, 91, 24, 73, 47, 87, 89, 15, 95, 81, 79, 
28, 19, 27, 26, 2, 54, 87, 2, 29, 9, 73, 85, 31, 94, 9, 18, 80, 27, 71, 97, 47, 68, 30, 10, 90, 71, 56, 24, 21, 1, 
100, 4, 88, 41, 15, 11, 21, 64, 2, 3, 75, 7, 16, 43, 45, 15, 62, 89, 47, 11, 84, 97, 15, 32, 7, 81, 93, 67, 33, 99, 
32, 47, 87, 53, 90, 93, 9, 24, 57, 44, 82, 14, 49, 93, 9, 36, 27, 8, 25, 34, 23, 41, 48, 100, 58, 68, 43, 34, 23, 52, 
53, 8, 11, 30, 87, 77, 44, 29, 85, 47, 76, 65, 82, 51, 83, 76, 86, 38, 68, 47, 23, 69, 8, 10, 98, 67, 77, 34, 2, 66, 
65, 16, 8, 11, 9, 46, 34, 46, 48, 45, 69, 10, 45, 10, 43, 55, 97, 52, 15, 19, 24, 64, 94, 9, 14, 4, 72, 88, 93, 86, 
58, 48, 48, 59, 18, 68, 86, 46, 1, 41, 26, 4, 29, 79, 85, 71, 61, 8, 76, 40, 22, 12, 50, 14, 39, 99, 73, 18, 46, 29, 
55, 69, 10, 27, 23, 82, 20, 88, 69, 48, 37, 18, 19, 55, 84, 64, 4, 23, 80, 21, 54, 69, 73, 49, 44, 58, 88, 93, 5, 89, 
68, 32, 13, 74, 7, 81, 90, 28, 98, 17, 76, 28, 70, 17, 18, 83, 77, 8, 97, 36, 94, 5, 8, 88, 6, 68, 19, 94, 3, 68, 18, 
69, 32, 70, 51, 18, 100, 9, 50, 73, 74, 8, 6, 10, 24, 28, 81, 31, 77, 78, 17, 92, 98, 76, 74, 98, 42, 33, 83, 68, 45, 
1, 65, 76, 27, 81, 70, 70, 79, 65, 3, 99, 45, 67, 80, 47, 56, 37, 94, 82, 73, 36, 8, 16, 95, 44, 35, 33, 43, 55, 100, 
91, 77, 82, 28, 9, 45, 18, 81, 58, 61, 81, 65, 46, 16, 73, 12, 10, 31, 66, 94, 100, 11, 59, 21, 62, 94, 2, 27, 60, 
85, 30, 23, 39, 44, 55, 1, 24, 22, 26, 5, 13, 50, 42, 96, 91, 3, 59, 21, 68, 33, 48, 33, 34, 2, 22, 47, 32, 14, 43, 
90, 82, 56, 52, 99, 24, 9, 33, 33, 56, 28, 1, 30, 62, 14, 55, 18, 69, 11, 35, 100, 26, 60, 7, 54, 5, 71, 78, 46, 31, 
61, 26, 19, 74, 6, 20, 59, 53, 28, 39, 77, 100, 76, 7, 5, 79, 57, 87, 92, 13, 36, 37, 34, 65, 54, 56, 82, 64, 11, 36, 
63, 11, 2, 12, 45, 32, 62, 13, 52, 49, 40, 20, 39, 87, 77, 74, 30, 26, 77, 52, 66, 62, 83, 15, 73, 75, 19, 92, 7, 59, 
37, 15, 47, 54, 55, 36, 70, 98, 45, 21, 87, 4, 8, 92, 63, 2, 97, 35, 41, 91, 74, 92, 7, 41, 48, 13, 51, 95, 21, 67, 
11, 30, 80, 51, 53, 10, 92, 64, 52, 49, 1, 27, 98, 84, 37, 99, 65, 87, 99, 66, 1, 85, 95, 16, 28, 81, 65, 9, 12, 56, 
2, 17, 91, 64, 52, 3, 33, 48, 72, 34, 84, 9, 4, 74, 40, 75, 42, 77, 64, 43, 11, 14, 16, 90, 66, 76, 22, 38, 92, 97, 
64, 21, 32, 53, 57, 56, 90, 70, 88, 69, 38, 79, 57, 80, 48, 67, 74, 45, 47, 9, 49, 16, 75, 27, 99, 11, 64, 47, 8, 6, 
17, 73, 22, 48, 6, 95, 32, 85, 92, 9, 33, 15, 35, 59, 20, 81, 65, 90, 57, 24, 90, 95, 90, 61, 48, 71, 46, 72, 4, 17, 
21, 48, 82, 68, 34, 72, 4, 57, 59, 34, 22, 18, 23, 78, 92, 34, 12, 10, 39, 48, 58, 85, 53, 64, 33, 50, 100, 11, 51, 
40, 60, 11, 85, 50, 68, 85, 65, 98, 15, 23, 5, 18, 24, 59, 22, 80, 9, 19, 68, 47, 20, 95, 88, 49, 91, 56, 91, 18, 90, 
94, 31, 27, 71, 14, 71, 83, 61, 97, 37, 76, 77, 25, 52, 79, 58, 58, 19, 17, 12, 25, 87, 58, 61, 98, 13, 31, 4, 55, 5, 
75, 2, 83, 63, 94, 35, 62, 98, 20, 6, 89, 78, 81, 79, 6, 47, 39, 90, 1, 18, 51, 91, 42, 95, 93, 55, 31, 7, 22, 97, 
63, 92, 28, 89, 71, 36, 96, 42, 64, 18, 88, 77, 51, 56, 51, 23, 58, 50, 47, 33, 93, 93, 15, 81, 30, 81, 85, 70, 88, 
100, 49, 79, 52, 37, 54, 28, 92, 46, 86, 86, 93, 20, 31, 26, 16, 34, 92, 62, 58, 10, 10, 100, 54, 95, 39, 78, 60, 67, 
8, 94, 29, 23, 5, 49, 75, 66, 31, 51, 41, 64, 77, 40, 52, 40, 23, 33, 86, 100, 80, 56, 59, 44, 79, 56, 6, 21, 9, 6, 
24, 18, 68, 3, 82, 74, 93, 52, 8, 85, 73, 80, 80, 75, 51, 72, 15, 56, 80, 85, 2, 26, 53, 68, 74, 60, 51, 11, 40, 67, 
60, 75, 49, 28, 34, 14, 95, 73, 14, 26, 11, 37, 20, 78, 1, 27, 60, 4, 54, 57, 53, 58, 62, 14, 65, 51, 9, 59, 99, 18, 
53, 93, 36, 86, 98, 5, 72, 52, 41, 77, 60, 98, 22, 4, 35, 17, 9, 43, 68, 4, 74, 32, 64, 25, 10, 65, 22, 41, 39, 88, 
100, 39, 58, 45, 87, 60, 92, 70, 92, 60, 18, 6, 82, 51, 38, 42, 93, 69, 21, 8, 84, 37, 22, 63, 12, 81, 54, 63, 91, 
54, 39, 37, 60, 39, 15, 35, 10, 69, 75, 94, 79, 49, 2, 100, 49, 50, 67, 59, 8, 56, 60, 39, 6, 89, 1, 63, 29, 41, 80, 
37, 33, 7, 45, 95, 72, 96, 91, 13, 61, 29, 44, 3, 94, 56, 46, 24, 44, 33, 13, 1, 77, 70, 37, 60, 90, 7, 66, 66, 82, 
98, 56, 39, 12, 91, 24, 73, 47, 87, 89, 15, 95, 81, 79, 28, 19, 27, 26, 2, 54, 87, 2, 29, 9, 73, 85, 31, 94, 9, 18, 
80, 27, 71, 97, 47, 68, 30, 10, 90, 71, 56, 24, 21, 1, 100, 4, 88, 41, 15, 11, 21, 64, 2, 3, 75, 7, 16, 43, 45, 15, 
62, 89, 47, 11, 84, 97, 15, 32, 7, 81, 93, 67, 33, 99, 32, 47, 87, 53, 90, 93, 9, 24, 57, 44, 82, 14, 49, 93, 9, 36, 
27, 8, 25, 34, 23, 41, 48, 100, 58, 68, 43, 34, 23, 52, 53, 8, 11, 30, 87, 77, 44, 29, 85, 47, 76, 65, 82, 51, 83, 
76, 86, 38, 68, 47, 23, 69, 8, 10, 98, 67, 77, 34, 2, 66, 65, 16, 8, 11, 9, 46, 34, 46, 48, 45, 69, 10, 45, 10, 43, 
55, 97, 52, 15, 19, 24, 64, 94, 9, 14, 4, 72, 88, 93, 86, 58, 48, 48, 59, 18, 68, 86, 46, 1, 41, 26, 4, 29, 79, 85, 
71, 61, 8, 76, 40, 22, 12, 50, 14, 39, 99, 73, 18, 46, 29, 55, 69, 10, 27, 23, 82, 20, 88, 69, 48, 37, 18, 19, 55, 
84, 64, 4, 23, 80, 21, 54, 69, 73, 49, 44, 58, 88, 93, 5, 89, 68, 32, 13, 74, 7, 81, 90, 28, 98, 17, 76, 28, 70, 17, 
18, 83, 77, 8, 97, 36, 94, 5, 8, 88, 6, 68, 19, 94, 3, 68, 18, 69, 32, 70, 51, 18, 100, 9, 50, 73, 74, 8, 6, 10, 24, 
28, 81, 31, 77, 78, 17, 92, 98, 76, 74, 98, 42, 33, 83, 68, 45, 1, 65, 76, 27, 81, 70, 70, 79, 65, 3, 99, 45, 67, 80, 
47, 56, 37, 94, 82, 73, 36, 8, 16, 95, 44, 35, 33, 43, 55, 100, 91, 77, 82, 28, 9, 45, 18, 81, 58, 61, 81, 65, 46, 
16, 73, 12, 10, 31, 66, 94, 100, 11, 59, 21, 62, 94, 2, 27, 60, 85, 30, 23, 39, 44, 55, 1, 24, 22, 26, 5, 13, 50, 42, 
96, 91, 3, 59, 21, 68, 33, 48, 33, 34, 2, 22, 47, 32, 14, 43, 90, 82, 56, 52, 99, 24, 9, 33, 33, 56, 28, 1, 30, 62, 
14, 55, 18, 69, 11, 35, 100, 26, 60, 7, 54, 5, 71, 78, 46, 31, 61, 26, 19, 74, 6, 20, 59, 53, 28, 39, 77, 100, 76, 7, 
5, 79, 57, 87, 92, 13, 36, 37, 34, 65, 54, 56, 82, 64, 11, 36, 63, 11, 2, 12, 45, 32, 62, 13, 52, 49, 40, 20, 39, 87, 
77, 74, 30, 26, 77, 52, 66, 62, 83, 15, 73, 75, 19, 92, 7, 59, 37, 15, 47, 54, 55, 36, 70, 98, 45, 21, 87, 4, 8, 92, 
63, 2, 97, 35, 41, 91, 74, 92, 7, 41, 48, 13, 51, 95, 21, 67, 11, 30, 80, 51, 53, 10, 92, 64, 52, 49, 1, 27, 98, 84, 
37, 99, 65, 87, 99, 66, 1, 85, 95, 16, 28, 81, 65, 9, 12, 56, 2, 17, 91, 64, 52, 3, 33, 48, 72, 34, 84, 9, 4, 74, 40, 
75, 42, 77, 64, 43, 11, 14, 16, 90, 66, 76, 22, 38, 92, 97, 64, 21, 32, 53, 57, 56, 90, 70, 88, 69, 38, 79, 57, 80, 
48, 67, 74, 45, 47, 9, 49, 16, 75, 27, 99, 11, 64, 47, 8, 6, 17, 73, 22, 48, 6, 95, 32, 85, 92, 9, 33, 15, 35, 59, 
20, 81, 65, 90, 57, 24, 90, 95, 90, 61, 48, 71, 46, 72, 4, 17, 21, 48, 82, 68, 34, 72, 4, 57, 59, 34, 22, 18, 23, 78, 
92, 34, 12, 10, 39, 48, 58, 85, 53, 64, 33, 50, 100, 11, 51, 40, 60, 11, 85, 50, 68, 85, 65, 98, 15, 23, 5, 18, 24, 
59, 22, 80, 9, 19, 68, 47, 20, 95, 88, 49, 91, 56, 91, 18, 90, 94, 31, 27, 71, 14, 71, 83, 61, 97, 37, 76, 77, 25, 
52, 79, 58, 58, 19, 17, 12, 25, 87, 58, 61, 98, 13, 31, 4, 55, 5, 75, 2, 83, 63, 94, 35, 62, 98, 20, 6, 89, 78, 81, 
79, 6, 47, 39, 90, 1, 18, 51, 91, 42, 95, 93, 55, 31, 7, 22, 97, 63, 92, 28, 89, 71, 36, 96, 42, 64, 18, 88, 77, 51, 
56, 51, 23, 58, 50, 47, 33, 93, 93, 15, 81, 30, 81, 85, 70, 88, 100, 49, 79, 52, 37, 54, 28, 92, 46, 86, 86, 93, 20, 
31, 26, 16, 34, 92, 62, 58, 10, 10, 100, 54, 95, 39, 78, 60, 67, 8, 94, 29, 23, 5, 49, 75, 66, 31, 51, 41, 64, 77, 
40, 52, 40, 23, 33, 86, 100, 80, 56, 59, 44, 79, 56, 6, 21, 9, 6, 24, 18, 68, 3, 82, 74, 93, 52, 8, 85, 73, 80, 80, 
75, 51, 72, 15, 56, 80, 85, 2, 26, 53, 68, 74, 60, 51, 11, 40, 67, 60, 75, 49, 28, 34, 14, 95, 73, 14, 26, 11, 37, 
20, 78, 1, 27, 60, 4, 54, 57, 53, 58, 62, 14, 65, 51, 9, 59, 99, 18, 53, 93, 36, 86, 98, 5, 72, 52, 41, 77, 60, 98, 
22, 4, 35, 17, 9, 43, 68, 4, 74, 32, 64, 25, 10, 65] 
start = t.time() 
print(listOne.count(69))
stop =t.time() 
print(stop-start) 
start = t.time() 
count = 0 
for i in listOne: 
    if i == 69: 
        count =  count + 1  
print(count) 
stop =t.time() 
print(stop-start)"""

# Play 3 -  Hacker rank Big sort
"""
def bigSorting(unsorted):
    numArray = list(map(int, unsorted))
    numArray.sort()
    strArray = list(map(str, numArray))
    return strArray


unsorted = ['6', '31415926535897932384626433832795', '1', '3', '10', '3', '5']
result = bigSorting(unsorted)
print(result)
"""

# Play 4 - Python Principles - Saving Calculator Project
"""
greeting = "Hello "
name = "Bob"

# Yearly Income
hourly_wage = 20
hours_per_week = 40
income_per_week = hourly_wage * hours_per_week
weeks_per_year = 48
income_per_year = income_per_week * weeks_per_year

# Yearly Spending
spend_per_week = 400
spend_per_year = spend_per_week * 52

# Yearly Savings
savings_per_year = income_per_year - spend_per_year

# Displaying Details
print(greeting+name)
print(name + "'s yearly income is:")
print(income_per_year)
print(name + "'s yearly spend is:")
print(spend_per_year)
print(name + "'s yearly savings:")
print(savings_per_year)

"""

# Play 5 - Python Principles Challenges |
"""
age = 35
days_in_year = 365
hours_lived = days_in_year * 24 * age
print(hours_lived)
"""

# Play 6 - Python Principles Challenges ||
"""
def f():
    return 0


print(f())


def b():
    return True


def is_ten(x):
    if x == 10:
        return True
    else:
        return False


def triple_and(a,b,c):
    return a and b and c


def different(x, y):
    if x != y:
        return True
    else:
        return False


def x(string):
    return int(string) + 3


def test_or_long(string):
    if string == 'test' or len(string) == 6:
        return True
    else:
        return False


def make_day_string(day):
    return "it is day {X} of the month".format(X=day)


def f(x):
    if x == 42:
        return True
    return False
"""

# Play 7 - python principles challenges |V
"""
def test(n):
    if n == 123:
        print("yay")
    else:
        print("nay")


test(123)
test(333)


def is_small(x):
    if x < 10:
        return True
    else:
        return False


def check(password):
    return password == "secret"


def max_health(mode):
    if mode == "easy":
        return 100
    elif mode == "medium":
        return 75
    else:
        return 35


def screen_height(device):
    if device == "nexus5x":
        return 732
    elif device == "iphone5":
        return 568
    elif device == "thinkpad":
        return 1080
    else:
        return -1


def special_birthday(age):
    if age == 18 or age == 21 or age == 100:
        return True
    return False


def valid_age(age):
    return 0 <= age <= 150


print(valid_age(43))


def decide(price):
    if price < 100:
        return "buy"
    if 100 <= price <= 150:
        return "hold"
    if price > 150:
        return "sell"
"""

# play 8 - python principles challenges V|
"""
def three_strings():
    return ["x", "y", "z"]


def is_valid(mode):
    mode_list = ["easy", "medium", "hard"]
    return mode in mode_list


def contains_42(sp):
    return 42 in sp


def second_item(sp):
    return sp[1]


def double(al):
    return al + al


def same_length(l1, l2):
    return len(l1) == len(l2)


def second_item(l):
    if len(l) > 2:
        return l[1]
    else:
        return -1


def first(l):
    return l[0][0]


def nested_lists():
    outer = [[1, 2, 3], ["a", "b", "c"]]
    return outer

"""

# Play 9 - print combination sum == 5
"""
allCombination = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            allCombination.append([i, j, k])


sum_5 = []
for i in allCombination:
    if sum(i) == 5:
        sum_5.append(i)


for i in sum_5:
    print(i)

"""

# Play 10 - python principles Challenges V|
"""
colors = ['red', 'green', 'blue']
for i in colors:
    print(i)

i = 0
while i < len(colors):
    print(colors[i])
    i = i + 1


var = 2
while var < 10000:
    var = var * 2

print(var)


def total_length(strings):
    l = 0
    for i in strings:
        l = l + len(i)
    return l


def product(single_parameter):
    product = 1
    for i in single_parameter:
        product = product * i
    return product


colors = [
    "red", "green", "blue",
    "purple", "cyan", "brown",
    "yellow", "silver", "gold"
]
for i in range(0, len(colors), 2):
    print(colors[i])
"""

# Play 11 - python principles Challenges V||
"""
sum_value = 0
for i in range(1, 100+1):
    sum_value = sum_value + i

print(sum_value)


for _ in range(20):
    for __ in range(20):
        print(_)
        print(__)


def positive_numbers(numbers):
    returnValue =[]
    for i in numbers:
        if i > 0:
            returnValue.append(i)
    return returnValue


def unique(stringParameter):
    returnValue = []
    for i in stringParameter:
        if i not in returnValue:
            returnValue.append(i)
    s = "".join(returnValue)
    return s


print(unique("fiwubfwe"))


def initials(name):
    returnValue = ""
    for i in name:
        if i.isupper():
            returnValue += i
    return returnValue


def add_until_0(stringParameter):
    returnValue = 0
    for i in stringParameter:
        if i == 0:
            break
        returnValue += i
    return returnValue

"""

# Play 12 -  python principles Challenges V||
"""
def get_tuple():
    return 32, 43


def first_three(listpara):
    return listpara[:3]


def concatenate_name(firstname, lastname):
    return firstname + " " + lastname


def special_birthday(birthday):
    return birthday[1] == 2 and birthday[2] == 29


def equal_coordinates(l):
    j = []
    for i in l:
        if i[0] == i[1]:
            j.append(i)
    return j


def trim(s, tn):
    return s[tn[0]:tn[1]]


def count(string):
    d = {}
    for i in string:
        if i not in d:
            d[i] = 1
        elif i in d:
            d[i] = d[i] + 1
    return d
print(count("Hello World"))

def keys_and_values(d):
    l = []
    k = list(d.keys())
    j = list(d.values())
    print(k)
    print(j)
    return l + k + j
print(keys_and_values({5: 87,
                       9: 98}))

"""

# Play 13 - Fake email finder
"""
def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."
    for i in string:
        if i not in valid:
            return True
    return False


def is_valid(email):
    if email.count("@") == 1:
        usr_name = email.split("@")
        if len(usr_name[0]) == 0:
            return False
        else:
            if has_invalid_characters(usr_name[0]):
                return False
            elif usr_name[1].count(".") == 1:
                domain = usr_name[1].split(".")
                if len(domain[0]) == 0:
                    return False
                else:
                    if len(domain[1]) == 0:
                        return False
                    else:
                        if has_invalid_characters(domain[0]):
                            return False
                        elif has_invalid_characters(domain[1]):
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False
"""

# Play 14 - Combination of list elements total to max_total
"""
min_limit = 1  # Static
no_of_numbers = 3  # Static
max_total = int(input("max_total:"))
max_limit = int(input("max_limit:"))

result = []
allPossibleList = []
for i in range(min_limit, max_limit+1):
    for j in range(min_limit, max_limit+1):
        for k in range(min_limit, max_limit+1):
            allPossibleList.append([i, j, k])
for i in allPossibleList:
    if sum(i) == max_total:
        result.append(i)
print(result)
"""

# Play 15 - permutations (not good for health)
"""
from itertools import permutations

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", 
'(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', 
'~', ' ']

perm = permutations(characters, 8)

for i in perm:
    j = "".join(i)
    print(j)

"""

# Play 16 - List of English alphabets (both uppercase and lowercase) and common symbols
"""
import string

all_chars = list(string.ascii_letters + string.digits + string.punctuation + " ")

print(all_chars)
"""

# Play 17 - weekly hackerrank
"""
import icecream as i
calorie = [5, 10, 7]
walk_distance = 0

for c in range(len(calorie)):
    m = max(calorie)
    calorie.remove(m)
    walk_distance = walk_distance + ((2**c)*m)

print(walk_distance)
"""

# play_18
"""
def unboundedKnapsack(k, arr):
    dp = [0] * (k + 1)
    for i in range(1, k + 1):
        for weight in arr:
            if weight <= i:
                dp[i] = max(dp[i], dp[i - weight] + weight)

    return dp[k]


n = sum([int(n[i]) for i in range(len(n))]) * k

return superDigit(str(n), 1) if n > 9 else n
"""

# Play 18 - Weekly coding
"""
n = 8
k = 5
contests = [[13, 1], [10, 1], [9, 1], [8, 1], [13, 1], [12, 1], [18, 1], [13, 1]]
importantContest = []
notImportantContest = []
for i in contests:
    if i[1] == 1:
        importantContest.append(i[0])
    else:
        notImportantContest.append(i[0])
luck = sum(notImportantContest)
win = 0
for _ in range(len(importantContest)-k):
    win += min(importantContest)
    importantContest.remove(min(importantContest))
luck = luck + sum(importantContest) - win
return luck
"""

# Play 19 - Leet code merge strings alternately
"""
word1 = "abc"
word2 = "pqr"
word = []
pointer0 = 0
pointer1 = 0
length = len(word1) + len(word2)
for i in range(length):
    if pointer0 != len(word1):
        word.append(word1[pointer0])
        pointer0 += 1
    if pointer1 != len(word2):
        word.append(word2[pointer1])
        pointer1 += 1
print("".join(word))
"""
"""
nums = [-2882,4968,-6121,5471,-40,-6717,1070,4403,2575,9682,9863,-1251,-6933,-3417,-5472,9332,-7907,3392,-776,-673,-4580
,3793,-5743,9673,8320,-6125,-7406,4464,-1254,-7052,9435,-6250,4438,-4530,3566,-6751,13,4706,-743,-9836,4905,-7293,-895,
1785,-9646,7278,-5477,-1741,4413,-1121,-5497,4898,-5305,-938,9383,-6754,8828,1326,586,3592,-7280,-965,-4328,-7577,-5790,
9341,-2573,2310,-6930,5555,-9208,-6111,-5279,4799,5690,461,-986,5753,-8336,4128,-2086,3813,-7562,-2727,-533,712,6186,
-9239,6528,-7753,8756,5087,3008,-930,2472,334,-6976,1653,-567,-2523,-2880,-6473,6203,8770,-3604,1354,-9567,5476,3648,
-407,8691,6278,-7632,-3454,4786,1996,-5811,-4036,-427,7892,1504,5243,8814,6541,8385,-904,685,6071,-3189,4739,-1866,8996,
-6034,659,5232,-7842,-8455,-7860,-7520,-6946,-5856,5359,5642,5779,9916,-7183,4945,-800,4796,7122,6901,-3987,7160,-3086,
-9390,7302,-7517,-4879,5479,1098,7754,1455,-6927,-7930,-3855,-3784,-2676,2329,3825,969,-5702,-5286,3481,8146,-6734,2118,
-6642,-2927,8783,5112,2068,702,-7254,3579,6629,9856,-561,4284,2542,577,256,-5752,-14,-5163,-5424,-962,-7170,9244,-4277,
8925,-5459,9957,-3301,928,2193,-4634,1929,-9317,5962,1650,-3382,-8191,4499,2841,4803,-9351,-7019,-574,-750,-2395,1352,
5182,-8696,9970,-1357,3152,6695,-7807,3435,4447,-4610,-2051,9299,9760,-6073,-3124,9952,3979,7569,-9715,6964,-5613,3310,
-3576,3081,-6293,9477,6872,1330,817,-3101,3862,5603,-7063,906,-318,21,9030,9144,7422,5965,4421,7518,8851,-4150,5422,
-8829,9608,-7373,7739,-3100,-7704,4476,3457,4380,-4239,-6999,1231,3012,-7232,-2272,6498,-4601,-6309,3091,9035,2218,
-7749,-7979,-9467,1601,-3389,6595,-4620,47,-3344,-6325,-7790,-3176,9614,7527,-4898,-7876,4995,934,3265,-9147,295,-2809,
-8887,3164,807,-5925,-6765,-8549,114,-9775,-3291,-2673,-5074,-7578,252,3496,2580,18,7683,1278,-7819,2435,-3633,8919,
3313,9079,-1205,3058,-6365,7716,5968,-9894,-9654,-7329,-1803,586,-5855,-9712,8663,-1850,3153,-7594,2577,6556,7186,657,
-4298,2835,8237,-1164,1817,-4525,-8469,-8672,4532,8694,-7100,-3304,7214,-2853,6783,3297,4189,6048,2252,8929,266,2174,
-6646,3096,-8839,-4512,-4816,2618,811,1894,-2265,-4896,-4513,-6285,2313,6440,-8582,-4773,9104,-9816,-9815,8709,-475,
6493,8485,-2823,-9852,2406,-2587,6666,6986,-8677,-2333,-9506,-5111,9119,-7939,-9983,4130,8266,9584,525,-7797,9479,764,
8724,2987,3802,-3931,2109,-9951,-2264,6300,8163,2231,8444,-3309,4346,6298,4825,1129,5993,4776,-5372,2314,-71,-6214,9312,
-487,-140,1820,2697,8869,-5728,-9490,-6884,8756,-9032,3651,-1748,9425,-1581,-6421,9095,6107,9089,9450,1351,1022,-7634,
1597,-604,5383,-560,-6353,-3224,-9318,-5275,-1942,-8819,-863,-7240,-7449,-8894,2809,559,7228,4796,-2093,-1476,131,727,
2571,2958,5574,-1606,-175,-9086,-114,950,580,-8023,-9653,-9296,-3954,-3582,8902,2125,75,-4359,-3807,-1506,7705,-4162,
-9432,-5011,-1613,-8215,-5726,4397,7290,4813,8284,5128,-8174,-8661,-6717,-7748,-7225,7220,7469,1742,-1801,1134,1428,
7583,-2642,5659,8211,2292,8876,-348,-3460,1665,9976,604,-9501,-4635,-6527,9262,-3184,4460,4748,4748,5686,-402,-9392,
-4082,988,4204,422,-1924,5415,-599,-6190,463,9857,6827,-9286,6806,6095,-4467,2234,7515,-8135,-1242,6157,-1051,-41,
-4098,1732,9960,2997,7627,3359,1018,3145,1271,3723,-5905,-5622,639,-3337,-1584,7462,6875,-3530,-2128,4262,7872,4973,
-8212,5553,-1149,7845,-7930,7773,-5993,-3686,4550,-334,7991,7909,-1131,-3957,6581,9759,2555,-574,-5781,-4845,-7558,
2633,6509,5617,3413,9037,3288,2756,8957,6460,1710,-1476,-6223,-4894,6881,3121,806,-9130,6590,-4094,-5734,-2153,-7982,
-2724,-7721,8884,-6497,7155,388,5667,-7618,5073,-2854,2232,-8069,6642,-5440,-5016,97,-1815,1250,1494,261,-5545,2008,
-4918,7912,5918,-6530,-6372,6804,-9193,745,-6551,-7879,-4665,6173,-2382,9371,490,7077,9571,-7659,-8356,6298,-8552,
-1106,1189,-8891,9428,-2991,2721,3227,-3382,449,412,7966,-1261,8486,7157,-8686,-4751,9287,3855,6286,1715,3680,-2029,
3024,2368,6665,9277,-3507,-4786,4177,-8851,8039,1063,4845,-674,1803,3793,314,7799,-3295,8170,-3310,-7252,8627,-7308,
-9477,-2982,4748,7812,9921,-6120,1987,6104,-6114,5648,1135,-6371,-7916,-4450,-1849,-7139,137,-2929,3909,-2636,-5613,
6822,-8251,4046,-2429,7976,-3223,3907,-3337,-6010,-9860,1481,7606,4702,-7014,9614,-2073,2119,2674,952,5824,-2760,9489,
1422,5918,8742,-3096,444,9356,-7730,4039,4974,9250,-4725,7021,-204,5401,-2934,1291,5083,3423,-346,8643,-682,8538,9464,
1441,-9122,-2982,8661,-990,6269,-7658,-8611,9167,3244,5190,-2035,-1551,-8749,-8262,-1855,2739,6774,6400,2820,3774,-5009,
173,-6641,-2055,6396,523,6461,5937,-7595,-7207,6010,4933,6270,-2451,-9359,-939,1509,1148,-1999,-1304,698,-9478,3356,
7520,3301,7780,-4638,9965,7486,-6711,-4610,11,4036,-5767,230,-9785,2854,6172,-7061,4978,-1541,9943,2136,-3453,9552,
-6779,-2462,-6427,-3026,-4319,-7799,7578,7805,8778,-3926,-646,-13,-504,6091,-6084,-1405,-4318,8382,3001,-979,5822,
-3548,-5655,1413,8540,8852,-7925,-5055,-1666,-7964,9721,8631,-3985,-807,5698,2780,514,-2662,6651,4479,704,7729,-4938,
-1770,6612,-6954,4454,7609,5671,12,4532,8698,-5405,-4851,-585,-3656,-3689,-9431,-4960,1662,604,-1112,1022,-757,2772,
-5630,-9011,-114,-9820,-7568,9225,-6721,21,-7641,8770,-3677,8355,8050,-2642,-8149,-7612,5866,2483,-9428,-3598,-1983,
-4340,6339,-4102,-5355,-2773,-1817,6358,-5318,-7479,-9401,1625,2395,-9690,9941,-8901,4822,-8681,7452,-4527,-6273,-7515,
6271,-5569,-6810,9621,1141,-3438,-2350,5791,9592,6534,-140,3596,-6711,9528,-6669,-238,8828,5275,-2361,-7619,-4486,-8194,
7860,1861,3918,-3870,-3843,2093,2524,206,1546,-2552,4795,-1572,-5537,-4928,3439,8340,2270,382,9561,4642,5008,7361,8089,
-3191,-5507,5090,7129,5505,9851,-1219,-2132,-2184,-2517,9402,6652,5289,-7644,4417,8760,-9522,4743,-449,-5499,18,7229,
-859,9578,8909,8739,4748,2230,7230,-511,-504,-7678,3255,5724,-6844,6758,-4340,740,-5124,2912,-1176,-5566,-6287,-920,
4373,-8511,7692,-1467,562,-7181,-4422,7769,-9812,114,-2096,2853,1978,-2205,-7429,-4452,1481,2176,8418,9628,-4476,
-535,-7735,-9979,7028,-964,-7884,5974,-144,-9403,-1626,9381,6289,-952,-2743,-4603,248,1733,5261,-2326,-66,3006,-7256,
2245,-2081,2070,-9373,4681,3917,-9824,-1973,-4837,9091,6978,-5764,7656,-3385,5408,6825,2825,-9607,5490,-3263,1319,5791,
-2550,237,8766,8047,-8376,9119,7381,4108,2605,-9220,-154,-6059,-3709,-4589,-3213,2268,7969,-647,-2917,5486,3399,8318,
-9804,-5261,-2001,9577,-7500,-1361,6166,5726,-7254,-8515,4756,3649,-4942,3505,-3491,433,-9355,-7285,9632,-2709,-9668,
-6632,5262,-8299,-6039,3939,-5356,728,2136,3597,-2353,-7326,-703,3005,8939,3039,-6428,-2619,7346,2693,5668,-5708,-3001,
-4388,875,-891,2167,-9856,168,2347,2856,-6058,8749,5952,-8919,-6563,-2293,-293,-1453,-8697,8670,5870,7297,-1109,-9315,
4236,-3534,-7633,-9166,5396,8907,-3390,-570,-8372,8013,-1839,1913,3023,-7803,-4830,6721,2082,-5342,4525,-4566,-9503,
-1105,6254,-5121,-6232,-7193,5874,-217,-8025,-5060,-6173,6979,-9638,-2753,2280,-3146,-6351,8149,6501,-6263,-276,160,
9642,7661,-200,9921,-7391,-9443,8606,9791,9626,-9459,-6129,9631,5224,4084,3928,-2713,-9850,-2828,8139,-1349,-6042,
-1330,4612,-9239,7682,-4711,7037,3518,-5961,4636,3206,169,-9117,-2807,-1278,4729,-3789,-5629,-8913,2132,-4458,1846,
4541,6757,-3691,2301,1453,-1551,8996,5946,-2391,7642,-1914,1484,-7650,-1362,726,2303,-349,5423,7457,-4070,-575,4862,
9418,-6177,3757,7726,2041,-3873,3341,-6035,-7459,-5124,776,2642,2458,-9146,7406,5365,7594,-1955,-549,-9051,-5388,-6186,
-508,-3589,-405,9321,-1048,-1137,3030,9502,2660,-4960,2027,9317,-1497,-7010,-2943,-6969,4339,1845,1010,-4508,-2524,2172,
-8792,-2639,-7115,1404,-1714,4612,-6123,9937,5596,6585,-9319,-5793,-9182,-1094,9696,-4128,5619,-1276,3274,4289,1689,
-2666,3679,7774,9208,8975,6084,6822,7314,-6338,-5014,7051,-1355,-813,-5113,-8606,-6300,862,-4656,9179,8221,-253,-730,
6576,8635,3050,-5506,-5332,1748,-8274,-4335,1888,9420,-2694,-3736,5887,7467,-695,2607,-8155,2384,4789,9042,-948,9486,
-2643,-2016,-4794,2703,-3927,-373,1104,-5408,-9233,2320,8007,3079,-9072,-3572,5443,322,-2326,-7471,7716,4289,7927,-7046,
-8689,66,-7192,2582,4301,1109,-8033,1654,-2732,-1012,-584,-1705,8207,8895,-5481,7493,-7514,1573,-3382,-1801,-3246,43,
3560,-296,-463,3716,7305,-3648,4268,-987,8438,-1659,2139,-4095,4633,9849,-6733,7841,193,1460,-2018,-1028,499,-1529]
k = 14538
op = float('-inf')
if len(nums) < k:
    print( sum(nums)/k)
else:
    for i in range(len(nums)):
        sums = 0
        if k+i > len(nums):
            break
        else:
            sums = sum(nums[i:k+i])
            op = max(sums, op)
print(op/k)

summ = sum(nums[:k])
ans = summ
print(len(nums))
print(ans)
for i in range(k, len(nums)):
    summ += nums[i] - nums[i - k]
    ans = max(ans, summ)
    print(ans)
print( ans / k)

print(sum(nums)/k)
"""
"""
import re

month = []


def updateLeapYear(year):
    if year % 400 == 0:
        month[2] = 29
    if year % 100 == 0:
        month[2] = 28
    elif year % 4 == 0:
        month[2] = 29
    else:
        month[2] = 28


def storeMonth():
    month[1] = 31
    month[2] = 28
    month[3] = 31
    month[4] = 30
    month[5] = 31
    month[6] = 30
    month[7] = 31
    month[8] = 31
    month[9] = 30
    month[10] = 31
    month[11] = 30
    month[12] = 31


def findPrimeDates(d1, m1, y1, d2, m2, y2):
    storeMonth()
    result = 0

    while True:
        x = d1
        x = x * 100 + m1
        x = x * 10000 + y1

        if x % 4 == 0 or x % 7 == 0:
            result = result + 1
        if d1 == d2 and m1 == m2 and y1 == y2:
            break
        updateLeapYear(y1)
        d1 = d1 + 1
        if d1 > month[m1]:
            m1 = m1 + 1
            d1 = 1
            if m1 > 12:
                y1 = y1 + 1
                m1 = 1
    return result


for i in range(13):
    month.append(31)

#  02-08-2025 04-09-2025   input
line = "02-08-2025 04-09-2025"
date = re.split('-| ', line)
d1 = int(date[0])
m1 = int(date[1])
y1 = int(date[2])
d2 = int(date[3])
m2 = int(date[4])
y2 = int(date[5])
output = findPrimeDates(d1, m1, y1, d2, m2, y2)
print(output)
"""

# play 20: Infosys springboard course
"""
def find_product(num1,num2,num3):
    product=0
    if(num1 == 7 or num2 == 7 or num3 == 7):
        if num1 == 7:
            product = num2 * num3
        elif num2 == 7:
            product = num3
        else:
            product = -1
    else:
        product= num1*num2*num3
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(4,7,3)
print(product)


def form_triangle(num1,num2,num3):
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    if num1+num2>num3 and num2+num3>num1 and num1+num3>num2:
        return success
    else:
        return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
form_triangle(num1, num2, num3)


def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0
    if rupees_to_make <= (no_of_five * 5 + no_of_one):
        five_needed = rupees_to_make // 5
        if five_needed > no_of_five:
            five_needed = no_of_five
        one_needed = rupees_to_make - (five_needed * 5)
        if one_needed > no_of_one:
            print(-1)
        else:
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
    else:
        print(-1)

# Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28, 8, 5)
"""

"""
def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0
    if quantity_ordered > 0 and distance_in_kms > 0:
        if food_type == "N":
            bill_amount = 150 * quantity_ordered
            if distance_in_kms <= 3:
                bill_amount += 0
            elif 3 < distance_in_kms <= 6:
                distance_in_kms -= 3
                bill_amount += (3 * distance_in_kms)
            else:
                distance_in_kms -= 6
                bill_amount += 9 + (6 * distance_in_kms)
        elif food_type == "V":
            bill_amount = 120 * quantity_ordered
            if distance_in_kms <= 3:
                bill_amount += 0
            elif 3 < distance_in_kms <= 6:
                distance_in_kms -= 3
                bill_amount += (3 * distance_in_kms)
            else:
                distance_in_kms -= 6
                bill_amount += 9 + (6 * distance_in_kms)
        else:
            bill_amount = -1
    else:
        bill_amount = -1
    return bill_amount


# Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount = calculate_bill_amount("N", 2, 7)
print(bill_amount)

def get_count(num_list):
    count=0

    for i in range(0,len(num_list)-1):
        if num_list[i] == num_list[i+1]:
            count += 1

    return count

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))
"""
"""
import time as t
arr = [915448231, 916719769, 917662837, 715015316, 711447205, 696727371, 627842906, 693323581, 589223635, 805654596, 289724826, 596391853, 677546381, 28255161, 678547833, 5033848, 779985432, 514350430, 272175782, 205770045, 543945020, 1844448, 224198429, 521732197, 908366382, 181958684, 675847307, 75968158, 958484570, 383664494, 932919694, 232764812, 332024687, 674016138, 288614336, 907551160, 293804054, 125334554, 353427546, 419094137]
start = t.time()
arr.sort()
print(arr[-1]*arr[-2])
stop = t.time()
print(stop-start)

start = t.time()
max1 = max(arr)
arr.remove(max1)
max2 = max(arr)
print(max1*max2)
stop = t.time()
print(stop-start)
"""
