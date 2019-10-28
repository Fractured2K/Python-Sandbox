# A class is like a blueprint for creating objects.
# An object has properties and methods(functions) associated with it.
# Almost everything in Python is an object


class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Extend class


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'


# Init user object
john = User('John Doe', 'john@doe.com', 24)

# You can instantiate multiple objects
janet = User('Jane Doe', 'Jane@doe.com', 24)
print(janet.name)

# Edit property
janet.age = 25
print(janet.age)

# Invoke method
janet.has_birthday()
print(janet.greeting())

# Init Customer
john = Customer('John Doe', 'john@joe.com', 40)
john.set_balance(500)
print(john.greeting())
