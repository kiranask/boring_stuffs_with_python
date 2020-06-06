word = "hippopotomush"
chars = []

# for w in word:
#     if w not in chars:
#         chars.append(w)
#     else:
#         print(f"{w} is occuring more than once")


from collections import Counter
word_len = Counter(word)
print(word_len)
# counter is dictionary
# key is char
# Value is the frequency

for key, value in word_len.items():
    if value >1 :
        print(f"{key} is happening {value} times")