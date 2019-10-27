# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
# import datetime = datetime.data.today();
import validator
from datetime import date
from time import time

today = date.today()
timestamp = time()
print(today)
print(timestamp)

# Custom

email = 'test@test.com'

if validator.validate_email(email):
    print('Email is valid')
else:
    print('Not an email')
