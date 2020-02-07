#!/usr/bin/env python3
# # find version
import sys
print(sys.version)
nl = '\n'
# -- Start Code --
#
print('\n  Contents of this Code File on Python Lists')
print('1) Lists are Ordered')
print('2) Lists can contain Arbitrary Objects')
print('3) Lists Elements can be accessed by Index')
print('4) Lists can be Nested')
print('5) Lists are Mutable')
print('6) Lists are Dynamic')

# 1) List are Ordered
print('\n  1) List are Ordered\n')
list_00 = []
print('list_00 is an empty list = ', list_00)
list_01 = ['val_00', 'val_01', 'val_02', 'val_03', 'val_04']
print('list_01 = ', list_01)
list_01_reversed = ['val_04', 'val_03', 'val_02', 'val_01', 'val_00']
print('list_01_reversed = ', list_01_reversed)
print("Does 'list_01' = 'list_01_reversed'? = ", list_01 == list_01_reversed)
print("Is 'list_01' also 'list_01_reversed'? = ", list_01 is list_01_reversed)
print('This shows the element order in lists matter & is not arbitary')

# 2) Lists can contain Arbitrary Objects
print('\n  2) Lists can contain Arbitrary Objects\n')
print('int = ', int)
print('len = ', len)
def foo():
    pass
print('foo function = ', foo)
import math
print('import math = ', math)
listArbObj = [int, len, foo, math]
print('listArbObj = [int, len, foo, math] = ', listArbObj)
# A list can contain the same object multiple times
listObjRepeat = [1, 100, 'val_01', foo, 1, 100, "val_01", foo]
print('Lists can contain the same object multiple times without errors, listObjRepeat = ', listObjRepeat)

# 3) List elements are accessed by Index (& are zero-indexed)
print('\n  3) List elements are accessed by Index (& are zero-indexed)\n')
# Individual list elements are accessed using an index number in square brackets
print('list_01 = ', list_01)
print('list_01[0] = ', list_01[0])
print('list_01[3] = ', list_01[3])
print('list_01[-1] = ', list_01[-1])
print('list_01[-3] = ', list_01[-3])
# Slicing in Lists (Remember zero-indexing)
print('  Slicing in Lists (Remember zero-indexing)')
listString = ['A', 'String', 'List', 'is', 'formed', 'this', 'Way']
# Index #'s:   0      1         2      3      4         5      6
# Index #'s:  -7     -6        -5     -4     -3        -2     -1
print('listString = ', listString)
print('listString[2:5] = ', listString[2:5])
print('listString[-5:-2] = ', listString[-5:-2])
print('listString[2:5] == listString[-5:-2] = ', listString[2:5] == listString[-5:-2], ' # Note: Equivilent list is formed whether positive or negative slicing')
# Omit first index to start slice at list beginning
# Omit second index to extend slice to list end
print('  Omit first index to start slice at list beginning AND,')
print('  Omit second index to extend slice to list end')
print('list_01 = ', list_01) #  ['val_00', 'val_01', 'val_02', 'val_03', 'val_04']
print('list_01[2:] = ', list_01[2:])
print('list_01[:2] = ', list_01[:2])
print('list_01[:2] + list_01[2:] = ', list_01[:2] + list_01[2:], 'The Complete List in order!')
# Stride is slicing by a determined amount (i.e. 2:5:2, Index 2 to 5, by 2-every other index)
print('list_01[0:4:2] = ', list_01[0:4:2])
print('list_01[4:0:-2] = ', list_01[4:0:-2])
print('list_01[0:4:-2] = ', list_01[0:4:-2], ' # Note: Index numbers must be reversed too')
print('list_01[::2] = ', list_01[::2])
print('list_01[::-2] = ', list_01[::-2])
# The [:] syntax & the difference between lists & strings
print('  The [:] syntax & the difference between lists & strings')
s = 'string'
print('s = ', s)
print('s[:] = ', s[:])
print('Is s[:] equal to s = ', s[:] is s, ', proving with a string, [:] returns a reference to the same object')
list = [1,2,3,4,5]
print('list = ', list, ', a list')
print('list[:] = ', list[:])
print('Is list[:] equal to list = ', list[:] is list, ', proving with a list, [:] returns a new object, a copy of the original list')
# 'in' and 'not in' operators
print("  'in' and 'not in' operators")
print('list_01 = ', list_01)
print('val_05 in list_01 = ', 'val_05' in list_01)
print('val_05 not in list_01 = ', 'val_05' not in list_01)
# 'concatenation (+)' and 'replication (*)' operators
print("  'concatenation (+)' and 'replication (*)' operators")
list_01 = list_01 + ['val_05', 'val_06']
print("list_01 + ['val_05', 'val_06'] = ", list_01)
print('list_01 = ', list_01)
print("list_01 * 2 = ", list_01 * 2)
# len(), min(), & max() functions
print("  len(), min(), & max() functions")
print('list_01 = ', list_01)
print('len(list_01) = ', len(list_01))
print('min(list_01) = ', min(list_01))
print('max(list_01) = ', max(list_01))
# Operate directly on a list literal
print('  Operate directly on a list literal')
print("['val_01', 'val_02', 'val_03'][2] = ", ['val_01', 'val_02', 'val_03'][2])
print("['val_01', 'val_02', 'val_03'][::-1] = ", ['val_01', 'val_02', 'val_03'][::-1])
print("'val_02' in ['val_01', 'val_02', 'val_03'] = ", 'val_02' in ['val_01', 'val_02', 'val_03'])
print("['val_01', 'val_02', 'val_03'] + ['val_04', 'val_05', 'val_06'] = ", ['val_01', 'val_02', 'val_03'] + ['val_04', 'val_05', 'val_06'])
print("len(['val_01', 'val_02', 'val_03', 'val_04', 'val_05', 'val_06'][::-1]) = ", len(['val_01', 'val_02', 'val_03', 'val_04', 'val_05', 'val_06'][::-1]))
print("Philip Curtis' Personal Computer' [::-1] = ", 'Philip Curtis\' Personal Computer' [::-1], 'A way to reverse a String!!')


# 4) Lists can be Nested
print('\n  4) Lists can be Nested\n')
listNested = ['level_01', ['level02_01', ['level03_01', 'level03_02'], 'level02_02', 'level02_03'], 'level01_02', ['level04_01', 'level04_02'], 'level01_03']
print('listNested = ', listNested)
print('listNested[0], listNested[2], listNested[4] = ', listNested[0], listNested[2],  listNested[4])
print('listNested[1] = ', listNested[1])
print('listNested[3] = ', listNested[3])
print('listNested[1][0] = ', listNested[1][0])
print('listNested[1][1] = ', listNested[1][1])
print('listNested[1][2] = ', listNested[1][2])
print('listNested[1][3] = ', listNested[1][3])
print('listNested[1][1][0] = ', listNested[1][1][0])
print('listNested[1][1][1] = ', listNested[1][1][1])
print('listNested[3][0] = ', listNested[3][0])
print('listNested[3][1] = ', listNested[3][1])
# Same syntax for indices & slices applies to all nested sublists
print('listNested[1][1][-1] = ', listNested[1][1][-1])
print('listNested[1][1:3] = ', listNested[1][1:3])
print('listNested[3][::-1] = ', listNested[3][::-1])
# Operators & functions apply only to the list at the specified level & are not recursive
print('listNested = ', listNested)
print('length of listNested = ', len(listNested),  ', Note: each sublist counts for only one index number')
# Let's look at these 5 individual indices, 3 strings & 2 sublists'
print('  \nLet\'s look at these 5 individual indices, 3 strings & 2 sublists')
print('listNested = ', listNested)
print('listNested[0] = ', listNested[0])
print('listNested[1] = ', listNested[1])
print('listNested[2] = ', listNested[2])
print('listNested[3] = ', listNested[3])
print('listNested[4] = ', listNested[4])
print('type(listNested[0]) = ', type(listNested[0]))
print('type(listNested[1]) = ', type(listNested[1]))
print('type(listNested[2]) = ', type(listNested[2]))
print('type(listNested[3]) = ', type(listNested[3]))
print('type(listNested[4]) = ', type(listNested[4]))
# Note: An individual element in a sublist does not count as an element of the parent list
print('  Note: An individual element in a sublist does not count as an element of the parent list')
print("'level03_01' in listNested = ", 'level03_01' in listNested)
print("'level03_01' in listNested[1] = ", 'level03_01' in listNested[1])
print("'level03_01' in listNested[1][1] = ", 'level03_01' in listNested[1][1])
print("'level03_01' in listNested[1][1][1] = ", 'level03_01' in listNested[1][1][1])
print("listNested[1][1].index('level03_01') = ", listNested[1][1].index("level03_01"))

# 5) Lists are Mutable
print('\n  5) Lists are Mutable\n')
print('list_01 = ', list_01)
# Modifying a single-list-value
print('  Modifying a single-list-value')
list_01[0] = 'start'
list_01[-1] = 'end'
print('list_01 = ', list_01)

# Strings do not handle assignment indexing, but do handle lookups
print('\n  Strings do not handle assignment indexing, but do handle lookups')
string = 'string'
try:
    s = 'string'
    s[2] = 'x'
    print(x)
except Exception as ex:
    print("Error from Try/Except code = ", ex)
print('string[1] = ', string[1])

# Delete a list Element
print('\n  Delete a list Element')
print('list_01 = ', list_01)
del list_01[-1]
print('del list_01[-1] (last element) = ', list_01)

# Modifying Multiple List Values
print('\n  Modifying Multiple List Values')
# use the slice assignment, list[#:#] = <iterable> (think of an iterable as a list)
# Element number inserted does not need to be equal to the number of elements replaced, lists grow or shrink as needed.  So insert multiple elements in place of a single element by using a slice denoting only one element.
print('list_01 = ', list_01)
list_01[0:3] = '00', '01', '02', '03', '04', '05', '06' # Note: Adds however many elementsbetween indexes 0-to-3
print('list_01[0:3] = ', list_01)
list_01[-1] = 'lastElement'
print('list_01[-1] = ', list_01)

# Insert Elements into a list without removing anything
print('\n  Insert Elements into a list without removing anything')
print('list_01 = ', list_01)
list_01[2:3] = ['elem_02', 'elem_03'] # enter in a new element at index 2
print('list_01 = ', list_01)

# Two ways to delete multiple elements (from the middle of a list)
print('\n  Two ways to delete multiple elements (from the middle of a list)')
list_01[2:4] = [] 
print("Delete 1: 'list_01[2:4] = []' = ", list_01)
del(list_01[6:]) # deletes from index#8 to end of list
print("Delete 2: 'del(list_01[6:])' = ", list_01)

# Prepending or Appending Items to a list using + concatenation & += augumented assignment Operators
print('\n  Prepending or Appending Items to a list using + concatenation & += augumented assignment Operators')
list_01 = [0, 1, 2]
print('list_01 = ', list_01)
list_01 += 'three', 'four' # adds elements to end of list (with or without [])
print('list_01 augumented assignment = ', list_01)
list_01 += [8] # adds an integer-element to list end, previous python versions caused errors
print('list_01 augumented assignment = ', list_01)
# A list must be concatenated with a object that is iterable
list_01 = ['-1', '-2'] + list_01 # concatenate with the existing list, extending it
print('list_01 concatenation with iterable = ', list_01)


# With the + operator, when concatating a list with an iterable, such as a string, the elements are broken out & added to the list individually
print('\n  With the + operator, when concatating a list with an iterable, such as a string, the elements are broken out & added to the list individually')
list_01 = [0, 1]
print('list_01 = ', list_01)
list_01 += ['string'] # this adds the entire string as one element in the list
print('list_01 concatenation wit string = ', list_01)
list_01 += 'string' #  added as 's', 't', 'r', 'i', 'n', 'g'
print('list_01 concatenation with string elements = ', list_01)

# Methods that Modify a List
# First, look a string modification for comparison to lists
# Note: Strings are immutable & therefore return a new string object modified by the coded method
s = 'string'
print("\n  String modification for comparison, s = ", s)
mod1 = s.upper()
print("original string, 's' = ", s, ', unchanged after modifcation code')
print("modified string, 'mod1' = ", mod1, ', which creates a new, uppercase string, leaving the original string unchanged')

# Lists a mutable so coded methods modify the original list
# Generic list append code: list.append(<obj>) # append object, <obj>, to the end of list
print('list_01 = ', list_01)
print("len(list_01) = ", len(list_01)) # =18
list_01.append('appended') # Note: more then one object causes TypeError
print('list_01 = ', list_01)
x = list_01.append(20)
print('x = list_01.append(20) = ', x) # Note: Remember, list methods modify the taget list in place, not return a new list.
print('type(x) = ', type(x))
print('list_01 = ', list_01)
print('type(list_01) = ', type(list_01))

list_01 = []
print('\nlist_01 = ', list_01)

# + Operator
print('\n  + Operator')
# print('list_01 = ', list_01) a list with an iterable, such as a string, the elements are broken out & added to the list individually
list_01 = list_01 + [1, 2, 3]
print('list_01 + [1, 2, 3] = ', list_01)

# .append operator
print('\n  .append operator')
# Note: .append() method adds an iterable as a single element, unlike the + operator
list_01.append([4, 5, 6])
print('list_01.append([4, 5, 6]) = ', list_01)
list_01.append('append')
print("list_01.append('append') = ", list_01) # code to extend a list with an intact string

# .extend Operator # adds an iterable to end of a list
# .extend() behaves like the += operator, since it modifies the list in place
list_01 = []
print('\n  .extend Operator')
print('list_01 = ', list_01)
# test the += operator vs. the .extend method
print('  test the += operator vs. the .extend method')
list_01.extend([7, 8, 9])
print('list_01.extend[7, 8, 9] = ', list_01)
list_01 += [10, 11, 12]
print("list_01 += [10, 11, 12] = ", list_01)
list_01.extend(['extend'])
print("list_01.extend['extend' ] = ", list_01)
list_01 += ["plusMinus"]
print("list_01 += ['plusMinus'] = ", list_01)
# compare <list_01.extend(['extend'])> vs. <list_01.extend('extend')> code results
# and
# compare <list_01 += ['plusMinus']> vs. <list_01 += 'plusMinus'> code results
list_01 = []
print('\nlist_01 = ', list_01)
list_01.extend(['extend'])
print("list_01.extend(['extend']) = ", list_01)
list_01.extend('extend')
print("list_01.extend('extend') = ", list_01)
list_01 = []
list_01 += ['plusMinus']
print("list_01 += ['plusMinus'] = ", list_01)
list_01 += 'plus'
print("list_01 += 'plus' = ", list_01) # Note: only quotes, no parenthesis
list_01 += ('Minus')
print("list_01 += 'Minus' = ", list_01) # Note: Quotes AND parenthesis, same result

# .insert Operator
print('\n  .insert Operator')
# Format: listName.insert(<index#>, <obj>)
# Note: Index # is the index you want the inserted object to become
list_01 = []
list_01.insert(0, 'index0')
print("list_01.insert(0, 'index0') = ", list_01)
list_01.insert(1, 'index1')
print("list_01.insert(1, 'index1') = ", list_01)
# ?? Insert multiple objects??

# .remove Operator
print('\n  .remove Operator')
# Format: listName.remove(<obj>) # Note: Error caused with no <obj> # Use Try/Except clause
print('list_01 = ', list_01)
list_01.remove('index1')
print("list_01.remove('index1') = ", list_01)



# POP IS NOT WORKING AS EXPECTED - REMOVING TWO ELEMENTS

# .pop Operator
print('\n  .pop Operator')

''' 
.pop differs from .remove in two ways
1. specify the index # of the element to remove, not the element itself
2. the .pop method returns a value of the element removed
'''
popList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('starting popList = ', popList)
popList.pop(5) # without an index#, removes the last list element
print("popList.pop() = ", popList.pop(), " = what the .pop removed")
print('popList.pop() = ', popList)
'''
popList.pop(4)
print("popList.pop(4) = ", popList.pop(4), " = what the .pop removed")
print('popList.pop() = ', popList)
'''





# 6) Lists are Dynamic
print('\n  6) Lists are Dynamic\n')
print('Lists are dynamic simply because lists actively grow or shrink as needed when elements are added or removed from them')

# Additional Notes_Experimenting on element types
print('\n**  Additional Notes  **')
print('  Experimenting on element types\n')
list_01 = ['val_01', 'val_02', 'val_03', 'val_04', 'val_05', 'val_06', 'val_07', 'val_08', 'val_09', 'val_10']
print('list_01 = ', list_01)
print('\n  Experimenting on element types:')
print('list_01 = ', list_01)
print('type(list_01[03]) = ', type(list_01[3]), ' , starting out as a string')
print('type(list_01) = ', type(list_01), ' , the original list, type unchanged')
list_01[3] = "list_01 last element"
print('\nlist_01 = ', list_01)
print('type(list_01[3]) = ', type(list_01[3]), ' , a string')
print('type(list_01) = ', type(list_01), ' , the original list, type unchanged')
list_01[3] = 100
print('\nlist_01 = ', list_01)
print('type(list_01[3]) = ', type(list_01[3]), ' , an integer')
print('type(list_01) = ', type(list_01), ' , the original list, type unchanged')
list_01[3] = 99.99
print('\nlist_01 = ', list_01)
print('type(list_01[3]) = ', type(list_01[3]), ' , a float')
print('type(list_01) = ', type(list_01), ' , the original list, type unchanged')
list_01[3] = 'val_12', 'val_13', 'val_14'
print('\nlist_01 = ', list_01)
print('type(list_01[3]) = ', type(list_01[3]), ' , a tuple')
print('type(list_01) = ', type(list_01), ' , the original list, type unchanged')
list_01[3] = ['val_12', 'val_13', 'val_14']
print('\nlist_01 = ', list_01)
print('type(list_01[3]) = ', type(list_01[3]), ' , a list')
print('type(list_01) = ', type(list_01), ' , the original list, type unchanged')
print('END Experimenting on element types\n')
