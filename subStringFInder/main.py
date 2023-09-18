string = input()
startvalue = 0
substring = []
length = len(string)
for i in range(0, length):
    for endvalue in range(i+1, length+1):
        substring.append(string[startvalue:endvalue])
    startvalue += 1
print(substring)
