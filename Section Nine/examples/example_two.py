# Example One of concept
# Outer function definition
def outer(a: int):
    a = a + 5
# inner function definition

    def inner(b: int):
        return b + 5
# Outer function returns the result of the inner function 
    return inner(a)
    
    
print(outer(5))


# Example Two of concept:  The inner function is aware of the a variable and does not 
# need it passed in 
def outer_two(a: int):
    a = a + 5
    
    # Inner Function definition
    
    def inner_two():
        return a + 5
    
    # Outer function returns the result of the inner function 
    return inner_two()

print(outer_two(5))
