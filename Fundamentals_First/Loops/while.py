is_learning = True

while is_learning:
    print("You're' learning")
#   is_learning = False # this checks if the condition is still True, which is not..so it breaks the loop
    user_input = input("Are you still Learning? (yes/no) ")
    is_learning = user_input == "yes"

print("ok you stopped learning")