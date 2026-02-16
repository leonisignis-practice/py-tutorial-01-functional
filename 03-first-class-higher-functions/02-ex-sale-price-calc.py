def calculate_price_20(price):
    return price * 0.8


print(calculate_price_20(100))  # Output: 80.0


def calculate_price_10(price):
    return price * 0.9


def calculate_clearance_price(price):
    return price * 0.5


# We can create a higher-order function that takes a discount function
# as an argument and applies it to the price.


def apply_discount(price, discount_func):
    return discount_func(price)


# This is repetitive and not very flexible,
# as we have to create a new function for each discount type.

# We can use higher-order functions to configure the three different discount functions
# also knows a a factory function, which is a function that creates and
# returns other functions based on some configuration.


def create_sales_calculator(percent_discount):
    def calculator(price):
        return price * (1 - percent_discount / 100)

    return calculator


twenty_percent_off = create_sales_calculator(20)
ten_percent_off = create_sales_calculator(10)
clearance_off = create_sales_calculator(50)

print(twenty_percent_off(100))  # Output: 80.0
print(ten_percent_off(100))  # Output: 90.0
print(clearance_off(100))  # Output: 50.0

# We can also use the apply_discount function with the created discount functions,
# but this is something we tried to avoid by creating the factory function,
# as it adds an extra layer of indirection.
print(apply_discount(100, twenty_percent_off))  # Output: 80.0
print(apply_discount(100, ten_percent_off))  # Output: 90.0
print(apply_discount(100, clearance_off))  # Output: 50.0
