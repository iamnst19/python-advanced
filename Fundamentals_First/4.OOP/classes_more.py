class Student: 
    def __init__(self, new_name, new_grades): #
        self.name = new_name #when you create a variable inside a class it is called a property, eg "name" property
        self.grades = new_grades #property of the object
    def average(self, name): #inside a class it is called a method and not a function
        return sum(self.grades) / len(self.grades) 

# Now we need to create the object, to create an object we call a class
student_one = Student("Rolf", [70, 88, 90, 99]) # new object of type student
student_two = Student("Jose", [50, 60, 99, 100])
#print(student_one.name)
#print(student_one.grades)

print(student_one.average())
#or
#print(Student.average(student_one))

def average(student):
    return sum(student.grades) / len(student.grades)
print(average(student_one))
