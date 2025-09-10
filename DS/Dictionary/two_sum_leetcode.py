def twoSum(self, nums, target):
    """
    :type nums: Li st[int]
    :type target: int
    :rtype: List[int]
    """
    dic = {}  # store numbers we have seen: number → index
    for i in range(len(nums)):

        if nums[i] not in dic:
            # If not seen before, store the partner we will need in future
            # Example: if target=9 and nums[i]=2,
            # then we will need 7 later. So store 7 → index_of_2
            partner = target - nums[i]
            dic[partner] = i

        else:
            # If yes → we found the pair!
            # dic[nums[i]] is the index of the first number
            # i is the index of the current number
            return [dic[nums[i]], i]
        # When you hit the else branch, the current number (nums[i]) is literally the partner you stored earlier. That’s why it passes.
        """
        🔎 Example again (target = 51, nums = [13, 4, 45, 6])

        At i=2, num=45 → partner = 6 → store {6:2}

        At i=3, num=6 → this nums[i] is equal to that partner (6).

        So dic[nums[i]] = dic[6] = 2.
        """