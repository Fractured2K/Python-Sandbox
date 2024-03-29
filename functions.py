# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Define function


def sayHello(name=''):
    """
    Prints Hello and then name.
    """
    print('Hello ' + name)


sayHello('')

# Return value


def getSum(a, b):
    total = a + b
    return total


numSum = getSum(4, 5)
print(numSum)


def addOneToNum(num):
    num += 1
    return num


print(addOneToNum(10))


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
getSum = lambda num1, num2: num1 + num2
print(getSum(9,2))
