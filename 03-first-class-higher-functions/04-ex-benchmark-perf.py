def double(x):
    # We could get a date time
    # start_time = datetime.now()
    # And then print the time it took to execute the function
    return x * 2


def square(x):
    return x * x


def greet(name):
    print(f"Hola, {name}!")


def test_function(func, *args, **kwargs):
    import time

    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    return result


# Benchmarking the functions
test_function(double, 10)
test_function(square, 3)
test_function(greet, "Leo")


def test_function2(func, *args, **kwargs):
    import datetime

    start_time = datetime.datetime.now()
    result = func(*args, **kwargs)
    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    print(f"Execution time: {total_time}")
    return result


# Benchmarking the functions
test_function2(double, 10)
test_function2(square, 3333333333)
test_function2(greet, "Leo")


# Using a factory
def create_benchmarker(func):
    def benchmarker(*args, **kwargs):
        import time

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result

    return benchmarker


double_bench = create_benchmarker(double)
square_bench = create_benchmarker(square)
greet_bench = create_benchmarker(greet)
double_bench(10)
square_bench(3333333333)
greet_bench("Leo")
print(greet_bench.__name__)

import functools


# Using a factory
def create_benchmarker(func):
    @functools.wraps(func)
    def benchmarker(*args, **kwargs):
        import time

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result

    return benchmarker


double_bench = create_benchmarker(double)
square_bench = create_benchmarker(square)
greet_bench = create_benchmarker(greet)
double_bench(10)
square_bench(3333333333)
greet_bench("Leo")
print(greet_bench.__name__)

# Using decorators


def benchmark(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result

    return wrapper


@benchmark
def double_bench(x):
    return x * 2


@benchmark
def square_bench(x):
    return x * x


@benchmark
def greet_bench(name):
    print(f"Hola, {name}!")


double_bench(10)
square_bench(3333333333)
greet_bench("Leo")
print(greet_bench.__name__)


# We can add more than one decorator
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"The {func.__name__} function is being called.")
        return func(*args, **kwargs)

    return wrapper


@benchmark
@logger
def double_bench(x):
    return x * 2


@benchmark
@logger
def square_bench(x):
    return x * x


@benchmark
@logger
def greet_bench(name):
    print(f"Hola, {name}!")


double_bench(10)
square_bench(3333333333)
greet_bench("Leo")
print(greet_bench.__name__)
