
def conditional_statements(n):
    if n%2 != 0:
        print("Weird")
    else:
        if 2<n<=5:
            print("Not Weird")
        if 6<n<=20:
            print("Weird")
        if n>20:
            print('Not Weird')

if __name__ == '__main__':
    N = int(input())
    conditional_statements(N)