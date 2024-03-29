#instance method takes the object ie ROLF as the first arguement
# Class Method --> Student or the class as the first arguement
# Another that takes nothing as the first arguement

class Student: 
    def __init__(self, name, school): #
        self.name = name 
        self.school = school
        self.marks = []
    def average(self): 
        return sum(self.marks) / len(self.marks) 

rolf = Student('Rolf', 'MIT')

rolf.marks.append(78)
rolf.marks.append(99)

print(rolf.average())

# Using Class Method
class Foo:
    @classmethod
    def hi(cls): #class method and the parameter will hold the value of the class it was called with ie Foo
        print(cls.__name__)

my_object = Foo()
my_object.hi() #the objects class gets printed out here

#Using Static Method
class Bar:
    @staticmethod
    def hi():
        print('Hi, I don\'t take parameters.')

another_object = Bar()
another_object.hi()
