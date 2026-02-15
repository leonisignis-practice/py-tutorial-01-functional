# Unpacking operator
# With lists
numbers_1 = [1, 2, 3]
numbers_2 = [4, 5, 6]

combined_numbers = [*numbers_1, *numbers_2]
print(combined_numbers)

person = {"name": "Leo", "age": 400, "color": "blue"}
person["color"] = "blue"  # This is imperative

updated_person = {**person, "color": "blue", "age": 401}
print(updated_person)


# Unpacking operator with arguments
def print_args(*args):
    print(f"The args are: {args}")


print_args(1, 2, 3)

numbers = [1, 2, 3, 4]
print_args(numbers)
print_args(*numbers)


def print_kwargs(*args, **kwargs):
    print(f"The args are: {args}")
    print(f"The kwargs are: {kwargs}")


print_kwargs(*numbers, **person)
