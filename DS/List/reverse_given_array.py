
# using for loop
def reverse_for(list ):
    reverse = []
    for i in range (len(list)-1, -1,-1):
        reverse.append(list[i])

    return reverse

# Using while loop
def reverse_while(list):
    lower = 0
    higher = len(list)-1
    while lower < higher :
        # Swap the elements
        list[lower], list [higher] = list[higher],list[lower]

        lower += 1
        higher -=1

    return list

list = [1,2,3,4,5,6]


