'''
Given an unsorted array of N elements and an element X. The task is to write a recursive function
to check whether the element X is present in the given array or not.

'''




#  search here is the given array
# lower is the lower bound in the array
# upper is the upper bound
# search is the element to be searched for
# lower and upper defines that search will be
#  performed between indices lower to upper

def recursion_search(arr, lower, upper, x):

    if lower > upper :
        return False

    if lower == x :
        return True

    if upper == x :
        return True


    return recursion_search(arr, lower +1 , upper -1 , x)




search_here = [1,2,3,4,5]
search = 8

print recursion_search(search_here,search_here[0], search_here[len(search_here)-1],search)