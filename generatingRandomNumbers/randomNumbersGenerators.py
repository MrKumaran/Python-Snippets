import random
import time


def randomNumberGenerator():
    return random.randint(1,1000_000_000)


if __name__ == '__main__':
    startTIme = time.time()
    limit = int(input("How many"))
    randomNumbers = []
    for i in range(limit):
        randomNumbers.append(randomNumberGenerator())
    stopTIme = time.time()
    print("Generated")
    print(randomNumbers)
    print("Time Taken =",stopTIme - startTIme)
