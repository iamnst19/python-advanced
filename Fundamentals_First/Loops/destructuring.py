#currencies = 0.8, 1.2
#usd, eur = currencies 

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]

for friend in friends:
    name, age = friend
    name = friend[0]
    age = friend[1]
    print(friends)

# Destructuring a Tuple
for name, age in friends: # each friend can also be taken as a name and an age
    print(f"{name} is {age} years old!")