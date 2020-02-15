from pythonds.basic.stack import Stack

""" 
balancing sysmbol problem

"""
given_string = "{([])}"
stack = Stack()

def balance_test(given_string):
    for char in given_string:
        if char in ["{","(","["]:
            stack.push(char)
        elif char in ["}",")","]"]:
            if stack.size() > 0 :
                top = stack.pop()
            else:
                return  False
            if top == "[" and char == "]":
                continue
            elif top == "(" and char == ")":
                continue
            elif top == "{" and char == "}":
                continue
            else:
                return False
        else:
            print("Something")
    if stack.size() == 0:
        return True
    else:
        return False
print(balance_test(given_string))





