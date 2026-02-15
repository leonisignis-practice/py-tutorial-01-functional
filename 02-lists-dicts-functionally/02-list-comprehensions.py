# List comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def double(x):
    return x * 2


# Similar to map
doubled_numbers = [double(x) for x in numbers]
print(doubled_numbers)

# SImilar to filter
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

big_numbers = [x for x in numbers if x > 5]
print(big_numbers)

times_five = [x * 5 for x in numbers]
print(times_five)
