def isPrime(num):
    for i in range(2, num):
        if num % i != 0:
            return True
        return False


if __name__ == '__main__':
    user_input = int(input('Enter Range: ')) # Getting input
    number = range(1, user_input)
    primes = list(filter(isPrime, number))
    print(primes)
