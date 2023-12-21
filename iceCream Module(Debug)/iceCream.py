# Importing ic from icecream module
from icecream import ic


# simple add function for demonstration
def add(number1, number2, number3):
    return number1 + number2 + number3


# Function to save run log into txt file
def logWrite(text):
    with open("Logs.txt", "a") as logFile:
        # write each log in new line
        logFile.write(text + '\n')


# ic prints argument as well as result in terminal which helps in debugging
ic(add(21, 321, 43))

# ic also returns value, so it can be used see value at some instance and also assigning value to variable
sumValue = ic(add(312, 213, 32))
print(sumValue)

# Empty IC
for _ in range(2):
    if _ == 1:
        # empty ic returns Filename, Line number, time the line executed
        # can be used to check whether it entered this block or not
        ic()
        continue
    else:
        print(_)

# also ic functions can be disabled for certain
print(ic(add(2, 4, 3)))
print(ic(add(3, 4, 3)))

# we can disable ic for certain lines if we know those lines are producing expected output
ic.disable()
print(ic(add(24, 4, 3)))
print(ic(add(23, 4, 3)))

# after disable we can again enable ic function
ic.enable()
print(ic(add(22, 4, 3)))

# Save run log in a separate txt file
ic.configureOutput(prefix="Runlog| ", outputFunction=logWrite, includeContext=True)

# after every ic.configuraOutput ic write its log into a file we mentioned
ic(add(21, 32, 31))
