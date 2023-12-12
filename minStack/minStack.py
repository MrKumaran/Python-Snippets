stack = []
top = -1


def minStack():
    pass


def push(element: int) -> None:
    global top
    stack.append(element)
    top += 1


def pop() -> int:
    global top
    element = stack.pop(top)
    return element


if __name__ == "__main__":
    while True:
        print("Select an operation to perform".center(50, "-"))
        print("\n\n")
        print("1 -> Push element to stack"
              "2 -> Pop element from stack"
              "3 -> Display stack"
              "4 -> Display Min stack"
              "Apart from these option will EXIT program.")
        user_input = int(input("Enter a number: "))

""" trying to build entire program on this topic. 
separate function to display options and get input from user
separate function to evaluate user input
separate function to display stack
separate function to display min stack

Go Beyond and try to implement class
"""
