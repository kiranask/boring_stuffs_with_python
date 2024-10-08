"""
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Input: [2,2,1]
Output: 1

Input: [4,1,2,1,2]
Output: 4

first += second

first = second + first

sum += sum1
xor:
0 0 0
0 1 1
1 0 1
1 1 0


"""


def find_unique(nums) -> int:
    first = nums[0]
    for i in range(1, len(nums)):
        first = nums[i] ^ first
    return first

def find_unique_number_from_dic(nums):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] =1
        else:
            dic[num] +=1
    for key, value in dic.items():
        if value ==1:
            yield key
nums=[10, 1, 1, 2, 9, 2]
for unique_number in find_unique_number_from_dic(nums):
    print(unique_number)


#print(find_unique([1, 1, 2, 9, 2]))
# print(find_unique([10, 1, 1, 2, 9, 2]))
"""
first = 1 ^ 1 = 0
first = 2 ^ 0 = 2
first = 9 ^ 2 = 11
first = 2 ^ 11 = 9

return 9 This is what happening!


"""