# Normal way (procedures/imperative)
numbers = [1, 2, 3]

for number in numbers:
    print(number)

# Procedural / Imperative
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)
print(doubled_numbers)


# map() function
# Declarative / Functional
def double(x):
    return x * 2


def add_5(x):
    return x + 5


doubled_numbers = list(map(double, numbers))
numbers_plus_5 = list(map(add_5, numbers))

print(doubled_numbers)
print(numbers_plus_5)

# The filter() funciton
# Declarative / Functional
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)


# Declarative / Functional
def is_even(x):
    return x % 2 == 0


evens = list(filter(is_even, numbers))

print(evens)

# Any function
is_any_even = any(map(is_even, numbers))

# All function
are_all_even = all(map(is_even, numbers))
all_even = all(map(lambda x: x % 2 == 0, numbers))

print(is_any_even)
print(are_all_even)
print(all_even)
