# program to find the odd age
ages = [22, 35, 41, 38, 59]
odds = [age for age in ages if age % 2 == 1]
print(odds)

# list of friends in upper and lower case intersecting using sets
friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Charlie", "michael"]

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

print(friends_lower.intersection(guests_lower))

#using list comprehension:
friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Jen", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]

present_friends = [
    name.title() for name in guests if name.lower() in friends_lower 
]
# also for code readability
""" present_friends = [
    name.title() 
    for name in guests 
    if name.lower() in friends_lower 
] """
print(present_friends)
