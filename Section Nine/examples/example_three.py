# Factorial recursive function
def factorial(n):
    if n == 1:
        return n 
    else:
        return n * factorial(n-1)


# Loop version of factorial function


def factorial_two(n):
    f = 1
    while n > 1:
        f = f * n 
        n = n - 1
    return f
        
