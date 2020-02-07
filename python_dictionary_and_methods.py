# python_Dictionary and Dictionary Methods
# Dictionaries are created with curly-brackets
# Dictionary format is dictionaryName = {'key':'value',
#                                        'anotherKey':'anotherValue',
#                                        'etc':'etc'}
# Dictionary keys can be any immutable data type (numbers, strings, tuples)
# Dictionary values can be any data type
# A key created with a mutable data type causes 'unhashable type' error

# Create a Dictionary
print('\nCreate a Dictionary')
dict_01 = {'key_01':'value_01',
           'key_02':'value_02',
           'key_03':'value_03',
           'key_04':'value_04',
           'key_05':'value_05'}
print('dict_01 = ', dict_01)   

# Access Values in a Dictionary (Note: Values, not Keys)
print('\nAccess Values in a Dictionary (Note: Values, not Keys)')
# Access values using the square brackets
print("Accessing the 3rd dictionary value via dict_01['key_03'] = ", dict_01['key_03'])
# Note: Trying to access a key that doesn't exist results in a 'KeyError'

# Add a Key-Value Pair to a Dictionary
print('\nAdd a Key-Value Pair to a Dictionary')
dict_01['key_06'] = 'value_06'
print('dict_01 with key_06 & value_06 added = ', dict_01)   

# Update a Key-Value Pair in a Dictionary
print('\nUpdate a Key-Value Pair in a Dictionary')
dict_01['key_01'] = 'value_00'
print('Updated key_01-value in dict_01 =', dict_01)
# Note: If only updating the key, & not the value, simply leave the value the same

# Delete a Key-Value Pair in a Dictionary
print('\nDelete a Key-Value Pair in a Dictionary')
del dict_01['key_01']
print('Delete Key-Value Pairs, key_01 & value_01, in dict_01 = ', dict_01)

# Dictionary Methods
print('\nDictionary Methods')
print('  1) Update Method')
print('  2) Get Method')
print('  3) Pop Method')
print('  4) Keys Method')
print('  5) Values Method')
print('  6) Items Method')

# Update Method
# Useful for updating multiple key-value pairs simutaneously by taking the dictionary as an argument
print('\nUpdate Method')
dict_01.update({'key_01':'value_01', 'key_00':'value_00', 'Apple':'Banana'})
print('Update method adding key-value pairs, 00 & 01, to dict_01 = ', dict_01)
# Note: key-value pairs added unordered

# Get Method
print("\nGet Method (dictionaryName.get('keyName'))")
print("Get method using 'dict_01.get('key_00')' = ", dict_01.get('key_00'))
# Note: If key or value do not exist, python returns 'None'. This is useful way to look up keys which may not be in the dictionary
#  i.e.: dict_01.get('key_25') returns 'None', while dict_01['key_25'] returns a KeyError
# Use Get method & specify a default value instead of 'None'
print("Use Get method & specify a default value instead of 'None' = ", dict_01.get('key_25', 0))

# Pop Method # removes a Key & returns that Keys Value
print("\nPop Method (dictionaryName.pop('keyName'))")
dict_01.pop('key_00')
print("dict_01 after pop('key_00') = ", dict_01)

# Keys Method # returns all dictionary keys
print("\nKeys Method (dictionaryName.keys())")
print(dict_01.keys())

# Values Method # returns all dictionary values
print("\nValues Method (dictionaryName.values())")
print(dict_01.values())

# Items Method # returns a kist-like object of tuples where each tuple is of the form: ('key':'value')
print("\nItems Method (dictionaryName.items())")
print(dict_01.items())


# Iterate through a Dictionary in two ways, a forLoop or the Keys method
print('\n\nIterate through a Dictionary in two ways, a forLoop or the Keys method')
# Iterate through a Dictionary Keys using a forLoop
print('Iteration via forLoop:')
for key in dict_01:
    print(key)
# Iterate through a Dictionary using the Keys Method
print('Iteration via Keys Method:')
for key in dict_01.keys():
    print(key)
# Iterate through a Dictionary using the Items Method accessing one key-value pair with each iteration
print('Iterate through a Dictionary using the Items Method accessing one key-value pair with each iteration')
for key, value in dict_01.items():
    print(key, value)

# END