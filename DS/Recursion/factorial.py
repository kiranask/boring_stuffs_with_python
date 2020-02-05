def factorial_generator(n):

    if n == 0:
        return 1

    return n*fibonacci_generator(n-1)


print(factorial_generator(5))


