my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99],    
    'average': None #something here #inorder to have a function living inside a dictionary , 
                    #a dictionary cannot have a function
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])


#print(average_grade(my_student))
# Object stores data and perform actions

#Class is something that defines what objects are
#with class we are just defining the object
class Student: #inside the class we are going to define two functions
    def __init__(self, new_name, new_grades): #here init is a dunder function, self here is an empty new object
        self.name = new_name #self is an empty object and inside it we are defining the name!
        self.grades = new_grades
    def average(self):
        return sum(self.grades) / len(self.grades)

# Now we need to create the object, to create an object we call a class
student_one = Student("Rolf", [70, 88, 90, 99]) # new object of type student
student_two = Student("Jose", [50, 60, 99, 100])
print(student_one.name)
print(student_one.grades)
print(student_two.name)
print(student_two.grades)
print(student_one.__class__) #defines which class its called from