def is_sorted(list):
    if len(list) <=1:
        return True
    else:
        return  list[0]< list[1] and is_sorted(list[1:])
print(is_sorted([1,2,3,5,6]))