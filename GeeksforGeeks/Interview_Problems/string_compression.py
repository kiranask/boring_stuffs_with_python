
def string_compresser(str1):
    compress = ''
    counter = 1
    for i in range(len(str1)-1):
        if str1[i] == str1[i+1] :
            counter +=1
        else:
            compress += str1[i] + str(counter)
            counter =1
    compress += str1[i] + str(counter)
    return  compress

print(string_compresser('aaabbccaa'))