number = int(input())
def print_prime(number):
    if number > 1:
        for number in range(2, number):
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                print(number, end=" ")


print_prime(number)
