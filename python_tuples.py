#!/usr/bin/env python3
# # find version
import sys
print(sys.version)
# -- Start Code --
'''
A Tuple is an ordered collection of objects
  Tuples are identical to Lists (ordered, contain arbitrary objects, can be indexed, sliced, & nested) except for two differences
    1) Tuples are defined by enclosing elements in parentheses( () ), instead of square brackets ( [] )
    2) Tuples are immutable (unchangable), instead of mutable as lists are
Reasons to use a tuple instead of a list:
    1) Program execution is faster
    2) Do not want data to be modified
    3) Can be used in a Dictionary, which requires one components value be immutable
 '''
tuple = ('zero', 'one', 'two', 'three')
print('\ntuple = ', tuple)

# Indexing & slicing tuples use square bracket ( [] ), the same as lists & strings
print('\n  Indexing & slicing tuples use square bracket ( [] ), the same as lists & strings')
print('tuple[0] = ', tuple[0])
print('tuple[-1] = ', tuple[-1])
print('tuple[1::2] = ', tuple[1::2])
print('tuple[::-1] = ', tuple[::-1], ' (reversing a tuple works the same as with a list)')

# Defining a Singleton Tuple
print('\n  Defining a Singleton Tuple (only 1 element)')
# Define empty tuple
t = ()
print("t = () = ", t, ' (empty tuple)')
print('type(t) = ', type(t))
# Define multiple element tuple
t = (1, 2, 'three', 'four', 5)
print(" 't = (1, 2, 'three', 'four', 5)' = ", t, ' (multiple element tuple)')
print('type(t) = ', type(t))
# Define an integer (no comma)
t = (1)
print(" 't = (1)' = ", t, ' (Interger, Note: no trailing comma)')
print('type(t) = ', type(t))
# Define Singleton tuple (trailing comma)
t = (1,)
print(" 't = (1,)' = ", t, ' (Singleton Tuple, Note: the trailing comma defines a Singleton Tuple)')
print('type(t) = ', type(t))

# Tuple Assignment, Packing, & Unpacking
print('\n  Tuple Assignment, Packing, & Unpacking')
print('tuple = ', tuple, "(The elements in the tuple are considered 'packed' into the object called 'tuple')")
print('tuple[0] = ', tuple[0], '(packed zero index element)')
print('tuple[-1] = ', tuple[-1], '(packed end element)')
# When a 'packed' object is assigned to a new tuple, the individual elements are 'unpacked' into the objects in the tuple
print("When a 'packed' object is assigned to a new tuple, the individual elements are 'unpacked' into the objects in the tuple (I.E.: '(e1, e2, e3, e4) = tuple')")
(e1, e2, e3, e4) = tuple
print('e1 = ', e1)
print('e2 = ', e2)
print('e3 = ', e3)
print('e4 = ', e4)
print("e1, e2, e3, e4 = ", e1, e2, e3, e4)
# Note: When unpacking, the number of variables on the left must match the number of values in the tuple
print("Note: When unpacking, the number of variables on the left must match the number of values in the tuple")

# Parentheses are not always needed with Tuples # If unsure, included parenthesis
print('\nParentheses are not always needed with Tuples. If unsure, included parenthesis')
t = 1,2,3
print('t = ', t)
x1, x2, x3 = t
print('x1, x2, x3(=t) = ', x1, x2, x3)
print('t = ', t)
x1, x2, x3 = 4, 5, 6
print('x1, x2, x3(= 4, 5, 6) = ', x1, x2, x3)
print('t = ', t, ', t still equals 1,2,3 even though x1,x2,x3 has been reassigned to 4,5,6')

# Swapping variables in Tuples
print('\n Swapping variables in Tuples')
variable1 = 'var1'
variable2 = 'var2'
print('variable1, variable2 = ', variable1, variable2)
print('Now the swap:')
variable1, variable2 = variable2, variable1
print(" 'variable1, variable2 = variable2, variable1' so 'variable1, variable2' = ", variable1, variable2)
# Note: With most other programming languages, to do this swap, a temporary variable must be used to hold the 2nd value in memory, not with Python.









