# sets comprehension
friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Charlie", "michael"]

friends_lower = {f.lower() for f in friends}
guests_lower =  {g.lower() for g in guests}

present_friends = {name.title() for name in friends_lower.intersection(guests_lower)}

print(present_friends)

#Program to print a dictionary from 2 lists with the provided conditions

friends = ["Bob", "Rolf", "Jen", "Anne"]
time_since_seen = [3, 7, 9, 2]

long_timers = {
    friends[i] : time_since_seen[i] # dictionary comprehensions
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

print(long_timers)

# the zip function -- bind two lists into dict[("Rolf", 3), ("Bob", 7), ("Jen", 15), ("Anne", 11)]
friends = ["Bob", "Rolf", "Jen", "Anne"]
time_since_seen = [3, 7, 9, 2]

long_timers = dict(zip(friends, time_since_seen))

print(long_timers)

# though the 3rd list is longer the zip function evicts the last
long_timers = list(zip(friends, time_since_seen, [1, 2, 3, 4, 5]))

print(long_timers)

#ENUMERATE Function

friends = ["Rolf", "John", "Anna"]

for counter, friend in enumerate(friends, start=1): # to start it at 1
    print(counter)
    print(friend)

print(list(enumerate(friends)))
#or
print(list(zip([0, 1, 2], friends)))

#for dict
print(dict(enumerate(friends)))
