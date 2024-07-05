# Play 1 - relational expression
"""
import re

# print('Hello'+'Ko')
lists = ["3", '', '#name', 'FirstName']
for i in lists:
    print(re.findall("\w+", i))
"""

# Play 2 - Time testing bw built-in count and for-if
"""import random as r import time as t listOne = [22, 41, 39, 88, 100, 39, 58, 45, 87, 60, 92, 70, 92, 60, 18, 6, 82, 
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


# play_18
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
