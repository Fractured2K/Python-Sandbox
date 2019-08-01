# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}
print(person)

# Using a constructor
person = dict(first_name='John', last_name='Doe', age=30)
print(person)

# Access value
print(person['first_name'])
print(person.get('first_name'))

# Add key/value
person['phone'] = '555-555-555'
print(person)

# Get keys
print(person.keys())

# Get items
print(person.items())

# Make copy
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

# Remove item
del person['age']
person.pop('phone')
print(person)

# Length
print(len(person2))

# Clear
person.clear()
print(person)

# List of dictionaries
people = [
    {'name': 'Mary', 'age': 40},
    {'name': 'John', 'age': 20}
]

print(people)
print(people[1]['age'])
