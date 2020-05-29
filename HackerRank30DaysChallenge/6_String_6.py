# Enter your code here. Read input from STDIN. Print output to STDOUT
#
def answer_string(strin):
    left, right = '', ''
    for i in range(len(strin)):
        if i % 2 == 0:
            left += strin[i]
        else:
            right +=  strin[i]
    print(left + " " + right)



answer_string("hacker")