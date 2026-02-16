def double(x):
    print("The double function is being called.")
    return x * 2


def square(x):
    print("The square function is being called.")
    return x * x


def greet(name):
    print("The greet function is being called.")
    print(f"Hola, {name}!")


answer = double(square(10))
greet("Leo")

# Instead of printing manually in every function,
# we can create a high order function


def create_printer(func, func_name):
    def printer(arg):
        print(f"The {func_name} function is being called.")
        return func(arg)

    return printer


double_printer = create_printer(double, "double")
square_printer = create_printer(square, "square")
greet_printer = create_printer(greet, "greet")

# Or
double_printer = create_printer(double, double.__name__)
square_printer = create_printer(square, square.__name__)
greet_printer = create_printer(greet, greet.__name__)

answer = double_printer(square_printer(10))
greet_printer("Leo")

# Using decorators, which are a special syntax in Python
# for applying higher-order functions to other functions.


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"The {func.__name__} function is being called.")
        return func(*args, **kwargs)

    return wrapper


@logger
def double_deco(x):
    return x * 2


@logger
def square_deco(x):
    return x * x


@logger
def greet_deco(name):
    print(f"Hola, {name}!")


answer = double_deco(square_deco(10))
greet_deco("Leo")

print(double_deco.__name__)  # Output: wrapper

# Using functools to create a decorator that can be applied
# to any function without losing its metadata.

from functools import wraps

# Or
import functools


def logger(func):
    # functools.wraps(func) is a decorator that updates the wrapper function
    # to look like the original function (func) in terms of its name, docstring, and other attributes.
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"The {func.__name__} function is being called.")
        return func(*args, **kwargs)

    return wrapper


@logger
def double_deco(x):
    return x * 2


@logger
def square_deco(x):
    return x * x


@logger
def greet_deco(name):
    print(f"Hola, {name}!")


answer = double_deco(square_deco(10))
greet_deco("Leo")

print(double_deco.__name__)  # Output: double_deco
