def sum_of_list_value_10(list):
    dictionary={}
    for i in range(len(list)):

        if (10-list[i]) in dictionary:

            print (list[i],10-list[i])

            # dictionary[list[i]] = dictionary[list[i]]+18
        else:
            dictionary[list[i]]=1
print( sum_of_list_value_10([1,2,3,4,6,9]))

