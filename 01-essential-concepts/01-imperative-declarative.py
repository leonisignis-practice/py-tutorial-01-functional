# Imperative vs. Declarative

# The imperative way:

numbers = [1, 2, 68, 27, 100, -4]

total1 = 0

for x in numbers:
    total1 += x

average1 = total1 / len(numbers)

print("The average is: ", average1)

# Or with a function


def imp_average(numbers):
    if not numbers:
        return 0

    total2 = 0

    for x in numbers:
        total2 += x

    average2 = total2 / len(numbers)

    print("The average is: ", average2)
    return


# The declarative way:

print(f"The average is: {sum(numbers) / len(numbers)}")

# Or using a function


def dec_average(numbers):
    return sum(numbers) / len(numbers)


print(f"The average is: {dec_average(numbers)}")
