numbers = [0, 1, 2, 3, 4]
doubled_numbers= []

for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers)

##OR
doubled_numbers = [number * 2 for number in numbers ] 
print(doubled_numbers)

# we can also use range for the above 
doubled_numbers = [number * 2 for number in range(5)]
print(doubled_numbers)

friend_ages = [22, 31, 35, 37]
age_strings = [f"My Friend is {age} years old" for age in friend_ages]

print(age_strings)

# string transformation to convert into lower characters
names = ["ROLF", "BOB", "JEN"]
lower = [name.lower() for name in names]
print(lower)

# EXAMPLE
friend = input("Enter your friend name:")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    friend_titlecased = friend.title() #title example Rolf (first letter and the rest is small)
    print(f"Congratulations you found {friend_titlecased}")
else: 
    print("sorry friend missing!")
