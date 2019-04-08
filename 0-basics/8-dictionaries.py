
myDict = {'Name': 'Vinay', 'Location': 'US', 'Pin': 12345}
# Update a value using the key
myDict['Name'] = 'Vinay Kumar'
# Add a new key-value pair
myDict['City'] = 'My City'

del myDict['Location']  # Delete a key-value pair
myDict.clear()  # Clear all the elements of myDict
del myDict  # Delete the dictionary

# Keys shouldn't be repeated
# If repeated, the last / latest assignment holds
# Keys in a dictionary must be immutable
# The keys can be a string / number / tuple . It couldn't be a list
# Linters warns about the duplicated key
myDict = {'Name': 'Vinay', 'Pin': 12345, 'Name': 'Vinay Kumar'}
print(myDict)

# Built In Functions and Methods
# len(myDict)
print(str(myDict))  # Printable string representation
print(myDict.get('Name'))
myDict.setdefault('ID', 111111)
# Sets to the value provided when the key is already not present
myDict.setdefault('Name', 'Test')
print(myDict.keys())
print(myDict.values())
print(myDict.items())
print(type(myDict.values()), type(myDict.keys()), type(myDict.items()))

# Including / Adding a dict to another
myDict2 = {'Year': 2000}
myDict.update(myDict2)
# Creating a sub dictionary from specific keys
print(myDict.fromkeys(('ID', 'Name'), 100))


# Mapping two lists to a dictionary
keys_list = [1,2,3,4]
vals_list = ['a','b','c','d']
dict_from_lists = dict(zip(keys_list,vals_list))

print(zip(keys_list, vals_list))
print(dict_from_lists)