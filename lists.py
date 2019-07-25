# A List is a collection which is ordered and changeable. Allows duplicate members.

# List definition
# numbers = [1, 2, 3, 4, 5]

# Using a constructor
numbers = list((1, 2, 3, 4, 5))

print(numbers)
print(type(numbers))

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Select array index
print(fruits[2])

# Length
print(len(fruits))

# Append to list
fruits.append('Mangos')
print(fruits)

# Remove from list
fruits.remove('Grapes')
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

# Remove from position
fruits.pop(3)
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# Sort list (Default alphabetic)
fruits.sort()
print(fruits)

# Reverse sort list
fruits.sort(reverse=True)
print(fruits)
