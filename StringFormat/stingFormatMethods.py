if __name__ == '__main__':
    message = 'Hello World!'

    # Different Methods of String Formatting!
    print(message, "Example 1")
    print(f'{message} Example 2')
    print("{} Example 3".format(message))
    print("%s Example 4" % message)
    print("{mg} {eg}".format(mg=message, eg="Example 5"))
    print("{0} {1}".format(message, "Example 6"))
