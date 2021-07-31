class Movie:
    def __init__(self, name, year): 
        self.name = name #self.name is not a variable it is a property of self and it is created inside of self
        self.year = year 

matrix = Movie('The Matrix', 1994)
print(matrix.name)
#or
print(Movie('The Matrix', 1994).name)
print("hi".__class__) #<class 'str'>

movies = ['Matrix', 'Finding Nemo']
print(len(movies))

