a = 10
b = 0
# While loop example - How many data objects are created?
# Recall that the integer is immutable.  What prints out?
while b <= 10:
    if b == 10:
        break
    b = b + 1
    
print(b)

# a letter list.  How many data objects are created?  Recall that the list is mutable
c = ['a', 'b', 'c', 'd', 'e', 'f']
c[3] = 'z'
#for loop example 
for item in c:
    if item == 'z':
        continue
    print(item)