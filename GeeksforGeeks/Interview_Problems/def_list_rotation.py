def rightRotate(lists, num):
    output_list = []

    # Will add values from n to the new list
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])
        print(item)
    # Will add the values before
    # n to the end of new list
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])

    return output_list


# Driver Code
rotate_num = 2
list_1 = [1, 2, 3, 4, 5, 6]

print(rightRotate(list_1, rotate_num))

def leftRotate(list, num):
    ouput_list = []
    len_ = len(list)
    for i in range(num, (len_)):
        ouput_list.append(list[i])
    for i in range (0, num):
        ouput_list.append(list[i])
    return ouput_list

print(leftRotate(list_1, rotate_num))

