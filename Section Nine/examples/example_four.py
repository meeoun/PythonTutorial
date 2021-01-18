# Generator function
def example(n):
    for i in n:
        yield i 

# yield returns an iterable object.
# This is why sum works.
print(sum(example([1, 2, 3, 4, 5])))