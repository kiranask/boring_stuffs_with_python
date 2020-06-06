Sentence="This is Testing"



def revese_words(sentence):
    low = 0
    list = sentence.split(" ")
    high = len(list) -1
    while low < high:
        list[low], list[high] = list[high], list[low]
        low +=1
        high -=1
    print(list)
    return " ".join(list)
print(revese_words(Sentence))






