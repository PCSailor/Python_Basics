# python_education_Sets & Set Theory
# Run this script to see examples

# Question: What's defination difference between unordered & ordered?

# Set Creation
print('# Set Creation')
# Empty Set
varMt = set()
# Sets with Values
varSetValues_01 = set(['listItem_01', 'listItem_02', 'listItem_03'])
# or
varSetValues_02 = {'curlyBraceItem_01', 'curlyBraceItem_02', 'curlyBraceItem_03', 'curlyBraceItem_04', 'curlyBraceItem_05', 'curlyBraceItem_06'}
print('varMt = ', varMt, '\nvarSetValues_01 = ', varSetValues_01, '\nvarSetValues_02 = ', varSetValues_02)


# Add Values to Sets (using 'varSetValues_01' from above)
print('\n# Add Values to Sets')
# Can only .add an immutable value (string or tuple) to a Set, not a list.
varSetValues_01.add('listItem_04')
print('varSetValues_01 = ', varSetValues_01)

# Remove Values from Sets (using 'varSetValues_02' from above)
print('\n# Remove Values from Sets')
# 4 Set Removal Methods
    # 1) .remove()
    # 2) .discard()
    # 3) .pop()
    # 4) clear()
# 1) .remove()
varSetValues_02.remove('curlyBraceItem_06')
print("varSetValues_02 after '.remove curlyBraceItem_06' = ", varSetValues_02)
# Note: Disadvantage of .remove is KeyError generated if value does not exist
# 2) .discard()
varSetValues_02.discard('curlyBraceItem_05')
print("varSetValues_02 after '.discard curlyBraceItem_05' = ", varSetValues_02)
# 3) .pop()
varSetValues_02.pop() # not sure what happens here
print("varSetValues_02 after '.pop curlyBraceItem_4' = ", varSetValues_02)
# 4) clear()
varSetValues_02.clear()
print("varSetValues_02 after '.clear()' = ", varSetValues_02)

# Iterate through a Set
print('\n# Iterate through a Set')
varSetValues_02 = {'curlyBraceItem_01', 'curlyBraceItem_02', 'curlyBraceItem_03', 'curlyBraceItem_04', 'curlyBraceItem_05', 'curlyBraceItem_06'}
print("varSetValues_02 reintialized = ", varSetValues_02)
print('Note: Iteration resulting in an unordered list')
for value in varSetValues_02: # resulting in an unordered list
    print('Iterating through a Set:', value)


# Transform a Set to Ordered Values
print('\n# Transform a Set to Ordered Values')
varOrderedSet = (['a', 'e', 'g', 'b', 'd', 'f', 'c'])
print("New 'varOrderedSet' initialized =", varOrderedSet)
print('type(sorted(varOrderedSet) = ', type(sorted(varOrderedSet)))
print('sorted(varOrderedSet, reverse = True) = ', sorted(varOrderedSet, reverse = True))
print('sorted(varOrderedSet, reverse = False) = ', sorted(varOrderedSet, reverse = False))

# Remove Duplicates from a List
print('\n# Remove Duplicates from a List, GO BACK AND MAKE NOTES HERE')
# Two appproaches
# 1) Create a Set from the List to remove duplicates
print('Create a Set from the List to remove duplicates resulting in Ordered List = ', list(set([1,2,3,1,7,2,4,4,8,2,6,4,1,5,3])))
# 2) Use List Comprehension to remove Duplicates from a List
def remove_duplicates(original):
    unique = []
    [unique.append(n) for n in original if n not in unique]
    return(unique)
print('Use List Comprehension to remove Duplicates from a List resulting in Unordered List = ', remove_duplicates([1,2,3,1,7,2,4,4,8,2,6,4,1,5,3]))
# Measuring the performace of both removal approaches
import timeit
# Approach #1 Execution Time
print(timeit.timeit('list(set([1,2,3,1,7,2,4,4,8,2,6,4,1,5,3]))', number=10000))
# Approach #2 Execution Time
print(timeit.timeit('remove_duplicates([1,2,3,1,7,2,4,4,8,2,6,4,1,5,3])', globals=globals(), number=10000))

# Set Operation Methods
print('\n\n# Set Operation Methods')
print('1) Union - Combine two sets into one')
print('2) Intersection - Set of all values common in both sets')
print('2b) Disjoint Set - True or False boolean for two sets with no values in common, or an empty intersection')
print('3) Difference')
print('4) Symmetric Difference - Set of values unique to one set, but not both')
# Start by initializing two sets (these will be unordered sets)
numbers_one = set(['one', 'two', 'three', 'four', 'five', 'six'])
numbers_two = set(['four', 'five', 'six', 'seven', 'eight', 'nine'])
print('numbers_one Set initialized = ', numbers_one, '\nnumbers_two Set initialized = ', numbers_two)

# Union (2 methods) # Combine two sets into one
numbers_union = numbers_one.union(numbers_two)
print('\nnumbers_union = ', numbers_union)
numbers_union_two = numbers_one | numbers_two
print('numbers_union_two = ', numbers_union_two)

# Intersection (2 methods) # Set of all values common in both sets
numbers_intersection = numbers_one.intersection(numbers_two)
print('\nnumbers_intersection = ', numbers_intersection)
numbers_intersection_two = numbers_one & numbers_two
print('numbers_intersection_two = ', numbers_intersection_two)
# Disjoint Set Boolean # two sets with an empty intersection or two sets with no values in common
# Initialize a set:
colors = {'red', 'blue', 'black', 'brown'}
print('Disjoint Sets of numbers_one & colors = ', numbers_one.isdisjoint(colors))
print('Disjoint Sets of numbers_one & number_two = ', numbers_one.isdisjoint(numbers_two))

# Difference (2 methods) # set of all values of one set that are not values of the other set
numbers_difference = numbers_one.difference(numbers_two)
print('\nnumbers_difference = ', numbers_difference)
numbers_difference_two = numbers_one - numbers_two
print('numbers_difference_two = ', numbers_difference_two)
# and reversed:
numbers_difference_reversed = numbers_two.difference(numbers_one)
print('numbers_difference_reversed = ', numbers_difference_reversed)

# Symmetric Difference (2 methods) # set of values unique to one set, but not both
numbers_symmetric_difference = numbers_one.symmetric_difference(numbers_two)
print('\nnumbers_symmetric_difference = ', numbers_symmetric_difference)
numbers_symmetric_difference_two = numbers_one ^ numbers_two
print('numbers_symmetric_difference_two = ', numbers_symmetric_difference_two)


# Set Comprehension
print("\n\nSet Comprehension for this list['one', 'two', 'one', 'two', 'one', 'two'] = ",  {skill for skill in ['one', 'two', 'one', 'two', 'one', 'two']})

# Membership Tests # Check if an element is contained in a sequence (strings, tuples, lists, or sets)
print('\nMembership Tests')
# In python, testing in Sets is more efficient then testing Lists
# Membership Test of a List
numbers_teen_list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
print('numbers_teen_list initialized = ', numbers_teen_list)
print("Membership Test for seventeen in numbers_teen_list = ", 'seventeen' in numbers_teen_list)
# Membership Test of a Set
numbers_set = {'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight', 'twenty-nine'}
print('numbers_set initialized = ', numbers_set)
print("Membership Test for eleven in numbers_set = ", 'eleven' in numbers_set)

# Subsets
print('Subsets')
numbers_set_mini = {'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 'twenty-four', 'twenty-five'}
print('numbers_set_mini initialized = ', numbers_set_mini)
print("Is 'numbers_set_mini' a subset of 'numbers_set'? = ", numbers_set_mini.issubset(numbers_set))

# Frozensets # A way to create nested sets
print('\nFrozensets')
# similar to a set except that it's immutable (unchanging) & cannot add or remove values
# Initiate a nested List & a nested Tuple
nestedLists = [['one', 1], ['two', 2], ['three', 3], ['four', 4], ['five', 5]]
nestedTuples = (('six', 6), ('seven', 7), ('eight', 8), ('nine', 9), ('ten', 10))
print('nestedLists initiated = ', nestedLists)
print('nestedTuples initiated = ', nestedTuples)
# nestedSets = set([set()]) causes a 'unhashable type: set' error
print("python cannot have nested sets, (i.e.: set([set()]) ), because sets cannot contain mutable (changing) values, so use frozensets instead\nnestedSets = set([set()]) causes a 'unhashable type: set' error")
# Initialize a frozenset
immutableFrozenSet = frozenset()
print('immutableFrozenSet = ', immutableFrozenSet)
nestedSets = set([frozenset()])
print('nestedSets = ', nestedSets)

# END