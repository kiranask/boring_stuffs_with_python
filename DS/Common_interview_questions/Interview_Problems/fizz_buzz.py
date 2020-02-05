# When Number is divisible by 3 print Fizz and when number is divisible by 5 print Buzz
# When Number is Divisible by both 3 and 5 print FizzBuzz

def fizz_buzz(n):
    for i in range(n):
        if i == 0 :
            print(i)
        if i > 0:
            if i % 3 == 0 and i % 5 == 0:
                print("fizzbuzz")
            elif i % 3 == 0 :
                print("fizz")
            elif i % 5 == 0:
                print("buzz")

            else:
                print(i)


print(fizz_buzz(60))