def sort(nums):
# firt loop for iterate over the first loop
# First Iteration: swap 6 elements
# Second Iteration: swap 5 elements
# Third Iteration: swap 4 elements
# .....
    for i in range(len(nums)-1,-1,-1):
        # First Time: total 6 swaps
        # Second 5 swaps
        # third 4 swaps
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] =nums[j+1]
                nums[j+1]= temp
nums = [2,1,3,45,5,3]
sort(nums)
print(nums)