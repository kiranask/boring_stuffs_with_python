#palindrome = str(input())

number = 122
string_number = str(number)
digits = [ int(char) for char in str(number)]

if digits == digits[::-1]:
    print(True)
else:
    print(False)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Step 1: Negative numbers can't be palindrome (e.g., -121 ≠ 121-)
        if x < 0:
            return False

        # Step 2: Convert number into list of digits
        # Example: 121 → ['1','2','1'] → [1,2,1]
        list_digits = [int(char) for char in str(x)]

        # Step 3: Compare digits with its reverse
        # If forward == backward → palindrome
        return list_digits == list_digits[::-1]
