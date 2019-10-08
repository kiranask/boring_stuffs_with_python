
def string_compresser(str1):
    compress = ''
    counter =1

    for i in range(len(str1)-1):
        if str1[i] == str1[i+1] :
            counter +=1
        else:
            compress += str1[i] + str(counter)
            counter =1
    compress += str1[i] + str(counter)
    return  compress


def string_comp(str1):
    ch = str1[0]
    compress = ''
    counter = 1

    for x in str1:
        if x == ch:
            counter = counter +1
        else :
            compress += str(ch) + str(counter)
            ch = x
            counter = 1

    return compress

print(string_comp('aaabbcc'))