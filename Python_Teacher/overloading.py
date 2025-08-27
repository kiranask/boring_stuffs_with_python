from boring_stuffs_with_python.Python_Teacher.dictonary_test1 import deathdays


def add_numbers(*args):

    return max(*args)


print(add_numbers(3,4,5,32723737))

# Am I audible now ?

def merge_dictionary(dict1, dict2):

    dict1.update(dict2)
    return dict1

dict1 = {1:2, 3:5}
dict2 = {2:4, 6:7}

print(merge_dictionary(dict1, dict2))