# Return index of nums whose sum is given target

nums=[2,15,16,7]
target= 9
def two_sum(nums, target):

    dict_seen = {}
    for i  in range(len(nums)):
        # get the current number
        num = nums[i]
        missing = target-num
        if missing not in dict_seen:
            dict_seen[num] = i
        else:
            return [i, dict_seen[missing]]
    return []



print(two_sum(nums, target))
