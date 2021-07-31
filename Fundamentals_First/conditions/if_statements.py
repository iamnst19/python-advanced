friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend: # if this condition is not True it quits the if loop
    print(f"Hello, {friend}")
    print("This runs too.")
else:
    print("Hello Stranger")

print("This runs anyways")

# the value of a number is True and 0 is False
print(bool(5))
print(bool(0)) """

""" name = input("Enter your name: ")

print(bool(name)) # the value of name is empty string then it is False
if name:
    print("We know your name.")

# this program checks if user exists
friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, friend")
elif user_name in family:
    print("Hello, family.")
else:
    print("I don't know you")
