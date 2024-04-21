import re

# Example contains some text
example = "exampleOne@gmail.com sents mail to exampleTwo@gmail.com"
# regular expression findall pattern in given argument(example) and ignore other all
print(re.findall("\w+@\w+\.\w+", example))
