"I have written logic to find out repeated words in given text"

def repeated_words(f_name):
    f_hand = open(f_name)

    word_dic = dict()

    for line in f_hand:
        words = line.split()
        for word in words:
            print (word)

            if word not in word_dic:
                word_dic[word] = 1
            else:
                word_dic[word] += 1

    for key, value in word_dic.items():
        if value > 1:
            print ("Repated Words are", key)


repeated_words('test.txt')




