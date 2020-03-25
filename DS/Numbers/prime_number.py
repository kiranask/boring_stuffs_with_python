# 2,3,5,7,11,

def is_primenumber(n):
    is_prime = True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
    return is_prime

print(is_primenumber(407))



