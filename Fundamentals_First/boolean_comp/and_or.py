## programming Age question
age = int(input("Enter your age:"))
can_learn_programming = age > 0 and age < 150
print(f"You can learn programming: {can_learn_programming}")


## Working problem

age = int(input("Enter your age:"))

#usually_not_working = age < 18 or age > 65
# not using a negative
usually_working = age >= 18 and age <= 65


print(f"At {age}, you are usually working: {usually_working}.")

## Print Bool
print(bool(35))
print(bool("Jose"))

## Print 
print(bool(0))
print(bool(""))

x = True and False
print(x)
x =  False or True 
print(x) 

x = 35 or 0
print(x) 

## Program with or
name = input("Enter your name: ")
surname = input("Enter your surname: ")

greeting = name or f"Mr. {surname}"
print(greeting)

## Not
print(not bool(35))
print(not 35)

# If the value on the left of the `and` operator is truthy, we get the value on the right of the operator.
x = True
cmp = x and 18
print(cmp)