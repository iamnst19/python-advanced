#the use of lambda is to transform the data to produce an output 
def divide(x, y):
    return x / y

#or , evne though is does not have an explicit return statement it takes the input and returns and output
divide = lambda x, y: x / y # if there is no name to this lambda function like the "divide", python will create and destroy immdeiatedly!
print(divide(15, 3))

#or
print((lambda x, y: x / y)(15, 3))

# Sample Use case of Lambda
def average(sequence):
    return sum(sequence) / len(sequence)

students = [
	{"name": "Hannah", "grades": (67, 33, 22, 83)},
	{"name": "Charlie", "grades": (91, 44, 23, 11)},
	{"name": "Peter", "grades": (71, 88, 21, 85)},
	{"name": "Rachel", "grades": (67, 79, 45, 44)},
	{"name": "Lauren", "grades": (54, 34, 99, 92)},
]

for student in students:
    print(average(student["grades"]))

#OR replace it with lambda
average = lambda sequence: sum(sequence) / len(sequence)

students = [
	{"name": "Hannah", "grades": (67, 33, 22, 83)},
	{"name": "Charlie", "grades": (91, 44, 23, 11)},
	{"name": "Peter", "grades": (71, 88, 21, 85)},
	{"name": "Rachel", "grades": (67, 79, 45, 44)},
	{"name": "Lauren", "grades": (54, 34, 99, 92)},
]

for student in students:
    print(average(student["grades"]))

