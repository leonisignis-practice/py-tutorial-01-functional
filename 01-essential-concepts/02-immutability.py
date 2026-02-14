# Immutability

# Variable names become a synonym for their value, and it will never changge
x = 5
# As in the case with pi
pi = 3.14159

# The imperative way
data = load_data_from_db()
# modify the data
for user in data:
    user["name"] = "ABC"
write_data_to_db(data)

# The declarative way
updated_data = map(lambda user: {**user, "name": "ABC"}, data)
write_data_to_db(updated_data)
