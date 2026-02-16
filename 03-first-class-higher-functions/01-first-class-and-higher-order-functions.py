def add_numbers(x, y):
    return x + y


print(add_numbers(3, 5))  # Output: 8

# Just like we can assign values to variables,
x = 4
message = "Hola"

#  we can also assign functions to variables.
my_function = add_numbers

# This is because functions are first-class citizens in Python.
print(my_function(10, 20))  # Output: 30

# Example
mode = "TEST"


def load_data1():
    if mode == "TEST":
        return [1, 2, 3]
    print("Loading data from a thrid-party API...")


# This would not be a pure function because it relies on the external variable `mode`.


# Let's try with a pure function instead:
def load_data_real():
    print("Loading data from a thrid-party API...")
    return [10, 20, 30]


def load_data_test():
    return [1, 2, 3]


mode = "PROD"

load_data = load_data_real if mode == "PROD" else load_data_test

data = load_data()

print(data)  # Output: [1, 2, 3]

# Passing function as an argument to another function


def subtract_numbers(x, y):
    return x - y


def operate_on_numbers(func, a, b):
    return func(a, b)


# This is a common pattern in Python and is often used in higher-order functions.
# This is called function composition.

print(operate_on_numbers(add_numbers, 5, 3))  # Output: 8
print(operate_on_numbers(subtract_numbers, 5, 3))  # Output: 2


def operate_10_and_11(func):
    return func(10, 11)


print(operate_10_and_11(add_numbers))  # Output: 21
print(operate_10_and_11(subtract_numbers))  # Output: -1

# Returning functions


def create_printer():
    def say_hello():
        print("Hola, World!")

    return say_hello


printer = create_printer()
printer()  # Output: Hola, World!

create_printer()()  # Output: Hola, World!

# The function retains its context,
# so it can access variables from the outer function
# even after the outer function has finished executing.
# This is a powerful feature of Python and is often used in functional programming.


def create_printer2():
    name = "Leo"
    # This is called a closure,
    # where the inner function retains access to the variables of the outer function.

    def say_hello():
        print("Hola,", name)

    return say_hello


printer2 = create_printer2()
printer2()  # Output: Hola,  Leo


# We can also create a more flexible printer function that takes a name as an argument
def create_printer3(name):
    def say_hello():
        print("Hola,", name)

    return say_hello


printer3 = create_printer3("Alice")
printer3()  # Output: Hola, Alice

# High order functions are functions that can take other functions
# as arguments or return functions as their result.
# Examples of higher-order functions in Python include `map`, `filter`, and `reduce`.
