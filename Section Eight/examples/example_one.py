# Dictionary a defined
a = {"first name": "john", "last name": "smith"}

# Dictionary b defined 
b = dict([['first name', 'jane'], ["last name", "wilson"]])

# Dictionary a updated with b contents
a.update(b)
print(a['first name'])

# New key added to dictionary
a['age'] = 20
print(a)

# Delete a key
a.pop('age')
print(a)

c = a

c['first name'] = 'joe'

# What prints out? why?
print(a['first name'])