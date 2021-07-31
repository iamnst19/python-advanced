class Student: #inside the class we are going to define two methods
    def __init__(self, name, school): 
        self.name = name         
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

""" class WorkingStudent:
    def __init__(self, name, school, salary):
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary
    def average(self):
        return sum(self.marks) / len(self.marks) """

# the working student class has everything common to the Student class and hence WorkingStudent can be treated as
# a child of Student
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
    def weekly_salary(self):
        return self.salary * 37.5
    

rolf = WorkingStudent('Rolf', 'MIT', 15.3)
print(rolf.salary)

rolf.marks.append(56)
rolf.marks.append(45)
rolf.marks.append(90)

print(rolf.average())
print(rolf.weekly_salary())

#lets define create an object anna for the class Stusent
anna = Student('Anna', 'Oxford')
print(anna.weekly_salary()) # thisgives an error as there is no weekly_salary in parent class!!
