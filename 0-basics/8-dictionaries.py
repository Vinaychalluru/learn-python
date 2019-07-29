
import traceback 

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

try:
    assert('State' in myDict.keys()), "Key Not Found"
    print(myDict['State']) # Throws KeyError when the Key is not found
except AssertionError as ae:
    print(f"Exception occurred {repr(ae)}")
    traceback.print_exc()
finally:
    print(myDict.get('State')) # Returns NoneType
    print(myDict.get('State', "N/A")) # dict.get() can be used to return a Default value when the Key is not found

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

# Standard Python dictionaries don't keep track of the order
# in which keys and values are added; they only preserve the
# association between each key and its value. If you want to
# preserve the order in which keys and values are added, use
# an OrderedDict

from collections import OrderedDict

fav_languages = OrderedDict()
fav_languages['Z'] = ['python', 'ruby']
fav_languages['Y'] = ['c']
fav_languages['R'] = ['ruby', 'go']
fav_languages['B'] = ['python', 'haskell']
# Display the results, in the same order they were entered.
for name, langs in fav_languages.items():
    print(name + ":")
    for lang in langs:
        print("- " + lang)

