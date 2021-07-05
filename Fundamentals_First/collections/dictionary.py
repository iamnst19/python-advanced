friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
# output value of the key 
print(friend_ages["Rolf"])

# add new entry
friend_ages["Bob"] = 20
print(friend_ages)

#change existing key
friend_ages["Rolf"] = 25
print(friend_ages)

# the difference between dictionaries and sets is that dictionaries keep the order
#but like sets you cannot have duplicate keys in dictionaries

# if you have multiple friends and have to store multiple data about them,
#use a tuple of dictionaries

friend = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Kiran Bala", "age": 29},
    {"name": "Jack Leesh", "age": 71}

)

# this will take away the burden of remembering or knowing the name of each friend

print(friend[0]["name"])
