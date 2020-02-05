def sentence_reverse(string):
    string = string.split(" ")
    reverse = ""
    for i in range(len(string)-1,-1,-1):
        reverse += string[i] + " "
    return reverse

print(sentence_reverse("I am the best man"))
