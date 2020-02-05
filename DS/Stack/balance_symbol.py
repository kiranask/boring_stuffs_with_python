from pythonds import Stack
stack = Stack()
open_par = ['{','(','[']
closed_par = [['}',']',')']]

def is_match(p1,p2):
    if p1 == '[' and p2 ==']':
        return True
    elif p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2== '}':
        return True
    else:
        return False

def balanced_symbol_validator(given_string):
    # Set two Flags
    is_balanced = True
    index = 0
    #When index is lesser than given string
    while index < len(given_string) and is_balanced:
        # Get the First Element of the String:
        parent = given_string[index]
        # If Open Parenthesis Push
        if parent in "{([":
            stack.push(parent)
        else :
            if stack.isEmpty():
                is_balanced = False
            else:

                top = stack.pop()
                if not is_match(top, parent):
                    is_balanced = False
        index +=1
        print(stack)

    if stack.isEmpty() and is_balanced:
        return True
    else:
        return False

print(balanced_symbol_validator("[["))






