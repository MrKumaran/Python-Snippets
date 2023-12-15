# Function to check primes Number
def isPrime(num):
    for i in range(2, num):
        if num % i != 0:
            return True
        return False


if __name__ == '__main__':
    # Getting input
    user_input = int(input('Enter Range: '))
    # generates array of input with range user_input
    number = range(1, user_input)
    # filter function pass each element to  function is prime and based on return bool it append to list
    primes = list(filter(isPrime, number))
    # printing primes
    print(primes)
