# Strings in python are surrounded by either single or double quotation marks.

# Variables
name = "Name"
age = 18

# Concatenate
print('Hello World I am ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by nnam
print('My name is {name} and I am {age}'. format(name=name, age=age))

# F-Strings (only in python 3.6+)
print(f'My name is {name} and I am {age}')

# String Methods
s = 'hello There world'

# Capitalize first letter
print(s.capitalize())

# Make all text uppercase
print(s.upper())

# Make all text lowercase
print(s.lower())

# Swap case
print(s.swapcase())

# Length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
print(s.count('h'))

# Starts with (Returns bool)
print(s.startswith('hello'))

# Ends with (Returns bool)
print(s.endswith('hello'))

# Split into a list
print(s.split())

# Find position (Returns int)
print(s.find('r'))

# Is all alphanumeric (Returns bool)
print(s.isalnum())

# Is all alphabetic (Returns bool)
print(s.isalpha())

# Is all number (Returns bool)
print(s.isnumeric())
