# Another concept of functional programming is using simple data structures


# Using a class
class Person:
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name


me = Person("Leo")
print(me.name)

# Instead, we build a simple data stucture such as a dictionary
person = {"name": "Leo", "age": 400, "color": "blue"}
print(person["name"])

# To change an attribute we need to do this using classes:
me.set_name("Leonis")  # Encapsulation
# or
me.name = "Leonis"  # Direct change

# But with a simple data structure we can do this:
person["name"] = "Leonis"

# Now  using functional programming

updated_person = {**person, "name": "Leonis"}

# This way it's easier to perform composition, mixing functions together


def get_name(dict):
    return dict["name"]


def uppercase(string):
    return string.upper()


print(person)
# We now combine them (composition)
print(uppercase(get_name(person)))

# This makes it flexible, making the functions available to other objects with
# the 'name' property

dog = {"name": "Rocky", "age": 3}

print(uppercase(get_name(dog)))

# First-class functions is another core concept of funcitonal programming
