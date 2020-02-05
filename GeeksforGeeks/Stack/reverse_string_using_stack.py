# Python program to reverse a string using Stack
# Function to create an empty Stack.
# It initializes size of Stack as 0

def createStack():
    stack = []
    return stack
# Function to determine the size of the Stack
def size(stack):
    return len(stack)


# Stack is empty if the size is 0
def isEmpty(stack):

    return stack == []

    # Function to add an item to Stack .


# It increases size by 1
def push(stack, item):
    stack.append(item)


# Function to remove an item from Stack.
# It decreases size by 1
def pop(stack):
    if isEmpty(stack): return
    return stack.pop()



# A Stack based function to reverse a string
def reverse(string):
    n = len(string)

    # Create a empty Stack
    stack = createStack()

    # Push all characters of string to Stack
    for i in range(0, n, 1):
        push(stack, string[i])

    # Making the string empty since all
    # characters are saved in Stack
    string = ""

    # Pop all characters of string and
    # put them back to string
    for i in range(0, n, 1):
        string += stack.pop()

    return string


# Driver program to test above functions
string = "GeeksQuiz"
string = reverse(string)
print("Reversed string is " + string)

# Another Method


print ("--------------------")
