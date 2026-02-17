# We can create a higher-order function that takes a function as an argument
# and returns a new function that tracks the number of times the original function is called.

import functools
import datetime
def print_stats(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        start = datetime.datetime.now()
        print(f"{func.__name__} has been called {wrapper.calls} times.")
        print(f"The function {func.__name__} was called with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"The function {func.__name__} returned: {result}")
        end = datetime.datetime.now()
        total_time = end - start
        print(f"{func.__name__} took {total_time}.")
        #return func(*args, **kwargs)
        return result

    wrapper.calls = 0
    return wrapper

def print_stats(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        total_time = end - start
        
        stats = {
            'args': args,
            'kwargs': kwargs,
            'result': result,
            'total_time': total_time
        }

        print(stats)

        return result

    wrapper.calls = 0
    return wrapper

@print_stats
def double(x):
    return x * 2

@print_stats
def square(x):
    return x * x

@print_stats
def add(x, y, z):
    return x + y + z

@print_stats
def greet(name):
    print(f"Hola, {name}!")

print(square(10))
print(add(1, 2, z=3))

print(double.__name__)
# Output: double.
# This is because we used functools.wraps in the print_stats decorator,
# which preserves the original function's metadata.
