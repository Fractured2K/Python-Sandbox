# A variable is a container for a value, which can be of various types

'''
This is a
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1             # Int
y = 2.5           # float
name = 'name'     # string
is_cool = True    # bool

# Multiple Assigment
x, y, name, is_cool = (1, 2.5, 'name', True)

# Basic Math
a = x + y

# Casting
x = str(x)
y = int(y)
z = float(y)

# Check type
print(type(x))   # '1'
print(type(y))   # 2
print(type(z))   # 2.0
