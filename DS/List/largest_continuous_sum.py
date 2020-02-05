def largest_cont_sum(list):
    cur_sum = 0
    max_sum = list[0]
    for i in range(len(list)):
        cur_sum = cur_sum + list[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum

print(largest_cont_sum([1,2,-1,3,4,10,10,7,-10,-1,6]))