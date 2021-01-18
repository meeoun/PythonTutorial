# Function that returns a dictionary type containing first and last name data
# Variables and data objects are local to the function only
def get_name(parcel: str):
    parcel = parcel.split()
    first = parcel[0]
    last = parcel[1]
    return {'first name': first, 'last name': last}
    

# get_name must be defined before called
# the variables/data objects used in the function definition
# are local to that function and can not be used outside
print(get_name("John Smith"))

# This line would fail.  First exists in the box of get_name
# and does not exist outside of it
print(first)