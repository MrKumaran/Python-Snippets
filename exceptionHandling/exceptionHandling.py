# infinity loop
while True:
    # try block execute code defined in it and if error occurs transfer control to except
    try:
        user_input = int(input("Enter a number: "))
        # if no error arises then break infinity loop
        break
    # if valueError arises except block will catch that error and prevent program from crashing
    except ValueError:
        # sends a user  warning message
        print("Invalid Enter Number ")


# after Breaking loop we can execute other block of codes like normal
print('Entered Number is', user_input)
