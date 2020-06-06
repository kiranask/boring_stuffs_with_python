def right_rotation(list,num):

    for i in range(num):
        temp = list[len(list) - 1]
        list.remove(temp)
        list.insert(0,temp)
    return list

print(right_rotation([1,2,3,4,5],2))