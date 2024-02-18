import random
import time
import sys

randomNumbers = []

""" 
Code won't work properly with recursion since it won't allow over 1000 times
"""

# generates RandomNumbers b/w 1 to 1 billion
def randomNumberGenerator(limit):
    if limit == 0:
        print(randomNumbers)
    else:
        randomNumbers.append(random.randint(1, 1000_000_000))
        randomNumberGenerator(limit-1)


# driver code
if __name__ == '__main__':
    limit = int(input("How many"))
    startTIme = time.time()
    randomNumberGenerator(limit)
    stopTIme = time.time()
    print("Time Taken =", stopTIme - startTIme)
