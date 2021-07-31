# this will iterate over the keys of the dictionary
friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}
for name in friend_ages:
    print(name)

# to iterate over the values
for age in friend_ages.values():
    print(age)

# structure the tuple as name and age
for name, age in friend_ages.items():
    print(f"{name} is {age} years old")