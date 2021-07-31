#add 2 numbers
def add(x, y=3): #if first param have default value all subsequent param must have default value
    total = x + y
    return total

print(add(5, 10))
print(add(x=3,y=2)) # inorder to pass without an error we need to give both x and y

#using named arguement 'sep' with built-in function print
print(1, 2, 3, 4, 5, sep='-')

######################
default_y = 3

def add(x, y=default_y):
    total = x + y
    print(total)

add(2)
default_y = 4 # here even if the variable is changed the func outputs the sum of prev var
add(2)