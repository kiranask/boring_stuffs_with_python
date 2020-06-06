# Enter your code here. Read input from STDIN. Print output to STDOUT

def answer_string(strin):
    left, right = '', ''
    for i in range(len(strin)):
        if i % 2 == 0:
            right += strin[i]
        else:
            left += strin[i]
    print(right + " " + left)


if __name__ == '__main__':
    number = int(input())
    for i in range(number):
        answer_string(input())




