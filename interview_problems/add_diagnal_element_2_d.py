


def add_diagnol_element_in2d_array(arr_2d):
    sum=0
    for i in range(len(arr_2d)):
        for j in range(len(arr_2d[i])):
            if i == j :
                sum += arr_2d[i][j]
    return  sum
arr_2d=[[1,2],[7,8]]
print (add_diagnol_element_in2d_array(arr_2d))

