class Student: #inside the class we are going to define two methods
    def __init__(self, name, school): 
        self.name = name         
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

# the working student class has everything common to the Student class and hence WorkingStudent can be treated as
# a child of Student
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
    @property #this decorator turns the method so we can use it by calling print(rolf.weekly_salary) 
    #instead of print(rolf.weekly_salary())
    def weekly_salary(self):
        return self.salary * 37.5
    

rolf = WorkingStudent('Rolf', 'MIT', 15.3)
print(rolf.weekly_salary) #the decorator has changed the no arguemnt method into a property or accessed it was a propterty