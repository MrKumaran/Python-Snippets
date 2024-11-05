"""
MinStack is a new data structure

minStack is originated from stack

its keeps track of minimum value

for example:

        stack = [1,2,3,-1,4]
     minStack = [1,1,1,-1,-1]

     meaning minStack will push if new value is minimum else it will push previous minimum value
     pop is same as stack
"""
import sys

# declaring stack, minstack, top as global
stack = []
minStack = []
top = -1


# function responsible for pushing element into stack
def push(element: int) -> None:
    # since we need to change global variable value we need to use global keyword
    # without global keyword we can only access global variable can't modify it
    global top
    # append element into stack
    stack.append(element)
    # if length of minstack is zero append directly to minstack
    if len(minStack) == 0:
        minStack.append(element)
    # if length of minstack is not zero
    # then append the minimum value between element and min-stack last element using min function
    else:
        minStack.append(min(element, minStack[-1]))
    # after pushing element into stack increment top
    top += 1


# function responsible for popping element from stack, minstack
def pop() -> tuple:
    global top
    # element hold pop element from stack and minstack in a tuple
    element = (stack.pop(top), minStack.pop(top))
    # after popping element from stack decrement top
    top -= 1
    # returns tuple
    return element


# display stack
def displayStack():
    print("Stack is ", stack)


# display minstack
def displayMinStack():
    print("MinStack is ", minStack)


if __name__ == "__main__":
    # infinity loop until manually give break statement. it's going to loop infinity
    while True:
        # menu for available operation and how to select operation
        print("Select an operation to perform".center(50, "-"))
        print()
        print("1 -> Push element to stack\n"
              "2 -> Pop element from stack\n"
              "3 -> Display stack\n"
              "4 -> Display Min stack\n"
              "Apart from these option will EXIT program.\n")
        user_input = int(input("Enter a number: "))
        # based on user_input it will perform operation
        if user_input == 1:
            push(int(input('Enter a Element: ')))
        elif user_input == 2:
            if top == -1:
                print("Stack is empty")
            else:
                stack_pop, minstack_pop = pop()
                print('Pop element from stack: ', stack_pop)
                print('Pop element from min stack: ', minstack_pop)
        elif user_input == 3:
            displayStack()
        elif user_input == 4:
            displayMinStack()
        # any other option that not in menu will exit the program
        else:
            sys.exit()
