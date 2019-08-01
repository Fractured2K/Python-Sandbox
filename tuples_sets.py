# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')
print(fruit_tuple)

# Using constructor
fruit_tuple_constructor = tuple(('Apple', 'Orange', 'Mango'))
print(fruit_tuple_constructor)

# Get value by index
print(fruit_tuple[1])

# Can not change values in tuple
# fruit_tuple[1] = 'Grape'

# Tuples with one value should have a trailing comma
fruit_tuple_trailing = ('Apple',)
print(fruit_tuple_trailing)

# Delete tuple
del fruit_tuple_trailing

# length
print(len(fruit_tuple))

# A Set is a collection which is unordered and unindexed. No duplicate members.
fruit_set = {'Apple', "Orange", 'Mango', 'Apple'}
print(fruit_set)

# Check if in set
print('Apple' in fruit_set)  # True
print('Apples' in fruit_set)  # False

# Add to set
fruit_set.add('Grape')
print(fruit_set)

# Remove from set
fruit_set.remove('Grape')
print(fruit_set)

# Clear set
fruit_set.clear()
print(fruit_set)

# Delete set
# del fruit_set
# print(fruit_set)
