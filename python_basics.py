# print statment
print("Hello World!")

#Memory Address
'''python takes same memory address, when two or more variables have same vales, id represents the address of the variable from memory'''
var1 = 0
var2 = 0
print(id(var1), id(var2))

#Delete variables in python
'''del var1,var2
print(id(var1), id(var2))'''

#type() function
'''By using python's build-in-function type(), we can know the data type of the variable'''
var3 = 55
var4 = 88.0
var5 = "faizal"
print(type(var3), type(var4), type(var5))


# Python data types
'''
  Numeric  - int, float, comples
  String   - str(text sequence type)
  Sequence - list, tuple, range
  Binary   - bytes, bytearray, memoryview
  Mapping  - dict
  Boolean  - bool
  Set      - set, frozenset
  None     - NoneType
  
'''

# Python Numeric data types

var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type ''' I don't more about this data type '''

# Python String data type

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string


# Sequence Data Types
''' Sequence is a collection data types. three sequence data types defined in Python'''
# List Data Type

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists
print ([list,tinylist])