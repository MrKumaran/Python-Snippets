import time

string = input()  # Getting input
startvalue = 0  # set Start value to Zero
substring = []  # List that holds substring of main string
length = len(string)
startTime = time.time()
for i in range(length):
    for endvalue in range(i + 1, length + 1):
        substring.append(string[startvalue:endvalue])  # Appending sliced string to substring list
    startvalue += 1
stopTime = time.time()
print(stopTime - startTime)
print(substring)
print(int(length * (length + 1) / 2))  # Maximum number substring possible
