# Pure Functions

# Example of 'impure' function

some_external_variable = 67


def my_function():
    return 1 + some_external_variable


print(my_function())
print(my_function())
some_external_variable = 99
print(my_function())

# We are changing the result of the function by changing an external variable

# Effects means changes made outside of a function's scope

some_var = 1


def effect_func():
    some_var += 1
    print(100)


# We can see that even though the function will always do the same thing, print 100
# it will change the value of a variable outside its scope

import random


def random_digit():
    return random.randint(0, 9)


print(random_digit())

# This is also an impure function

# It's not the purpose of functional programming to have zero imperative functions
# but as many pure functions as possible
