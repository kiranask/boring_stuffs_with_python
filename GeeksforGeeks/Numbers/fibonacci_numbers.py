def fibonacci_number_generator(n):
   sum = 0
   first = 1
   second = 1
   while sum < n :
       sum = first + second

       print(first)
       first = second
       second = sum
print(fibonacci_number_generator(100))


