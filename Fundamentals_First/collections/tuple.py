# tuple does not have square brackets but either represented with "()" or not brackets

short_tuple = "Rolf", "Anne"
short_tuple_with_brackets = ("Rolf", "Anne")

# brackets are also useful to differentiate when there is tuple inside a list
tuple_in_list = [("Rolf", "Anne")]
not_a_tuple = "Rolf" #this is a string

# you canmot append, add, insert to a tuple --> it is immutable 
##But we can add 2 tuples
friends = ("Rolf", "Anne", "Marco")
friends = friends + ("Jen",) #here the right side evaluates first
print(friends) #here it is not changed bu has rather created a new one which has 4 elements
