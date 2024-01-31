import random
import time
import sys


# generates RandomNumbers b/w 1 to 1 billion using generators
def randomNumberGenerator():
    yield random.randint(1, 1000_000_000_000)


# driver code
if __name__ == '__main__':
    startTIme = time.time()
    limit = int(input("How many"))
    randomNumbers = []
    for i in range(limit):
        randomNumbers.append(next(randomNumberGenerator()))
    stopTIme = time.time()
    print("Generated")
    print(randomNumbers)
    print("Time Taken =", stopTIme - startTIme)
    print("Size of randomNumberGeneratorFunction =", sys.getsizeof(randomNumberGenerator()))
