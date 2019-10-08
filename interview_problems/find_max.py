items =[6,20,19,56,23,87,41,49]

def find_max(items):
    if len(items) == 1:
        return items[0]

    op1 = items[0]


    op2 = find_max(items[1:])


    if op1 > op2 :
        return op1
    else :
        return op2
print (find_max(items))


