
"""

"""
def larger_than(str1,str2):

    if len(str1) > len(str2):

        return True
    elif len(str1)==len(str2):

        for i in range(len(str1)):

            if str1[i] > str2[i]:

                return True
            elif str1[i] == str2[i]:
                continue
            else:
                return False

    else :
        return False

print larger_than("213","212")