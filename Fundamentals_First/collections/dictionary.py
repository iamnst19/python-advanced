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
# but like sets you cannot have duplicate keys in dictionaries

# if you have multiple friends and have to store multiple data about them,
# use a tuple of dictionaries

friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Kiran Bala", "age": 29},
    {"name": "Jack Leesh", "age": 71}

)

# this will take away the burden of remembering or knowing the name of each friend

print(friends[0]["name"])
#OR

friend = friends[0]
print(friend["name"])

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

#turn lists of tuples to dictionary
friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27) ]
friend_ages = dict(friends)
print(friend_ages)

# Sample 
players = [
    {
        'name': 'Rolf',
        'numbers': (13, 22, 3, 6, 9)
    },
    {
        'name': 'John',
        'numbers': (22, 3, 5, 7, 9)
    }
]
print(players[0]['numbers'])
print(players[0]['numbers'][0]) 



# Question

lottery_numbers = {13, 21, 22, 5, 8}
#A player looks like this:
 
{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}
""" 
""" #Define a list with two players (you can come up with their names and numbers).

players = [
    {
        "name": "Rolf",
        "numbers": {1, 3, 8, 22, 21}
    },
    {
        "name": "Jose",
        "numbers": {4, 9, 10, 12, 15}
    }
]
 
# For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
# Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
# You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
# Then construct a string and print it out.
 
# Remember: the string must contain the player's name and the amount of numbers they got right!
name = players[0]["name"]
numbers = players[0]["numbers"].intersection(lottery_numbers)
print(f"Player {name} got {len(numbers)} numbers right.")
 
name = players[1]["name"]
numbers = players[1]["numbers"].intersection(lottery_numbers)
print(f"Player {name} got {len(numbers)} numbers right.")


# Joining a List
friends = ["Rolf", "Anne", "Charlie"]
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}.")