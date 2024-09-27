sentence = "I am Kiran Sk"
def rev(sen):
    reverse = []
    for word in sen.split(" "):
        reverse.append(word[::-1])
    return " ".join(reverse)
    # return  " ".join([word[::-1] for word in sen])

print(rev(sentence))



