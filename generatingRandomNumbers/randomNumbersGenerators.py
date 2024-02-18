import random
import time
import sys


# generates RandomNumbers b/w 1 to 1 billion
def randomNumberGenerator():
    return random.randint(1, 1000_000_000)


# driver code
if __name__ == '__main__':

    limit = int(input("How many"))
    randomNumbers = []
    startTIme = time.time()
    for i in range(limit):
        randomNumbers.append(randomNumberGenerator())
    stopTIme = time.time()
    print("Generated")
    print(randomNumbers)
    print("Time Taken =", stopTIme - startTIme)
    print(sys.getsizeof(randomNumberGenerator()))
