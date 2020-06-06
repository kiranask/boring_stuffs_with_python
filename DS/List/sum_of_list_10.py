def sum_of_list_value_10(list,target):
    dictionary={}
    for i in range(len(list)):
        if list[i] not in dictionary:
            dictionary[target-list[i]] = list[i]
        else:
            yield list[i], dictionary[list[i]]
        print(dictionary)
for items in sum_of_list_value_10([1,2,3,4,5,6,9],10):
    print(items)

