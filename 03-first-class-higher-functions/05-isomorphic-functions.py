# Isomorphic functions are functions that can be applied to both single values and lists of values.
# They are also known as "polymorphic functions" or "generic functions".
# In Python, we can create isomorphic functions using higher-order functions.

def double(x):
    return x * 2

def minus_one(x):
    return x - 1

def square(x):
    return x * x

print(double(10))
print(minus_one(10))
print(square(10))

# mapping to...

numbers = [1, 2, 3, 4, 5]
print(double(numbers)) # Output: [2, 4, 6, 8, 10]
print(minus_one(numbers)) # This will raise an error because we cannot subtract 1 from a list
print(square(numbers))

# In order to make the above code work, we can use the map function to apply the double,
# minus_one, and square functions to each element in the numbers list.

print(list(map(double, numbers))) # Output: [2, 4, 6, 8, 10]

# Using high order functions, we can create a new function that takes
# a function as an argument and applies it to each element in the list.

def apply_to_list(func, list):
    return [func(x) for x in list]

def list_or_value(func):
    def wrapper(arg):
        if isinstance(arg, list):
            return list(map(func, arg))
            # return [func(x) for x in arg]
        else:
            return func(arg)
    return wrapper

double_or_list = list_or_value(double)
minus_one_or_list = list_or_value(minus_one)
square_or_list = list_or_value(square)

print(double_or_list(numbers)) # Output: [2, 4, 6, 8, 10]
print(double_or_list(10)) # Output: 20

print(minus_one_or_list(numbers)) # Output: [0, 1, 2, 3, 4]
print(minus_one_or_list(10)) # Output: 9

print(square_or_list(numbers)) # Output: [1, 4, 9, 16, 25]
print(square_or_list(10)) # Output: 100
