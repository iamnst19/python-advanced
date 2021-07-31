# first class as you can give a function to a variable
def greet():
    print("Hello")
hello = greet

hello()

# create a function that calculate the average of a sequence
""" def average(seq):
    return sum(seq) / len(seq)
 """
 #instead of using a def/function, we can use a lambda to define the function like below 
#we may not need to keep the (seq) here and enter 'sum', 'len', 'max' 
avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq) 

operations = {
    "average": avg,
    "total": total,
    "top": top
}

students = [
	{"name": "Hannah", "grades": (67, 33, 22, 83)},
	{"name": "Charlie", "grades": (91, 44, 23, 11)},
	{"name": "Peter", "grades": (71, 88, 21, 85)},
	{"name": "Rachel", "grades": (67, 79, 45, 44)},
	{"name": "Lauren", "grades": (54, 34, 99, 92)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top':")
    
    operation_function = operations[operation]
    print(operation_function(grades))

#code block with conditions

#    if operation == "average":
#        print(avg(grades))
#    elif operation == "total":
#        print(total(grades))
#    elif operation == "top":
#        print(top(grades)) 