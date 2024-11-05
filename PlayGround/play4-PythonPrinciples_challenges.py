# Python Principles Challenges |

age = 35
days_in_year = 365
hours_lived = days_in_year * 24 * age
print(hours_lived)


# Python Principles Challenges ||

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


# Python principles challenges |V

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


# Python principles challenges V|

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


# Python principles Challenges V|

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


# Python principles Challenges V||

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


# Python principles Challenges V||

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
print(keys_and_values({5: 87, 9: 98}))

