import re
lists = ["3", '', '#name', 'FirstName']
for i in lists:
    print(re.findall("\w+", i))