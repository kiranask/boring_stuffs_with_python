def isValidSubsequence(array, sequence):
    # Write your code here.
    for i in range(len(array)):
        if array[i] in sequence:
            if array[i:(i + len(sequence))] == sequence:
                return "true"
            else:
                return "false"



def sub_seq(array, sequence):

    dict = {}
    for item in array:
        if item not in dict:

            





print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [10]))