"""
Need to return number of consecutive 1's occurs in a given binary string

for this, simple algorithm used is

checks by each character in string
                if equals to 0
                    restart the counter
                else
                    find max between counter variable and max consecutive 1's variable
                    and store it in consecutive 1's variable we are not going change this variable
                then finally return consecutive 1's variable
"""

def consecutiveOnesLength(binary):
    count = 0
    consecutiveOnes = 0
    # loop through each bit
    for bit in binary:
        # Reset count when 0 is found
        if bit == 0:
            count = 0
        # If 1 is found, increment count
        else:
            count += 1
            consecutiveOnes = max(consecutiveOnes, count)
    return consecutiveOnes


if __name__ == "__main__":
    user_input = input("Enter binary String: ")
    # splitting the input by space -> converting into int datatype -> mapping it and then converting it into list
    binaryList = list(map(int, user_input.split()))
    print(consecutiveOnesLength(binaryList))
