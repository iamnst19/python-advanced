# Generally we want to keep the lists homogeneous which is it should not contain int or other items like furnitures instead of friends
friends = ["Rolf", "Jose", "Babu"]
print(len(friends)) 
# another list of friends and their ages
friends = [["Rolf", 24], ["Bob", 30], ["Anne",27]]
print(friends[0][1])

# when we have a long list it is a good practice to put it into multiple lines

friends = [
    ["Rolf", 24], 
    ["Bob", 30], 
    ["Anne", 27],
    ["Charlie", 54],
    ["Jose", 17],
    ["Alex", 33],
]

print(friends[2][1])


#add/append to a list
friends = ["Rolf", "Jose", "Babu"]
friends.append("Jen")
print(friends)
friends.remove("Babu")
print(friends)
friends = [["Rolf", 24], ["Bob", 30], ["Anne",27]]
friends.remove(["Rolf", 24])
print(friends)