#IndexError
friends = ['Rolf', 'Anne']
friends[2] #IndexError: list index out of range 

#KeyError
def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['release']}") # should have been year

#Name Error
print(hello) #NameError: name 'hello' is not defined

# Attribute Error
## This error is very common when you play with objects
friends = ['Rolf', 'Jose', 'Anna']
friends_nearby = ['Rolf', 'Anna']
friends.intersection(friends_nearby)
#here we get attribute error as the listobject does not have intersection as an attribute

#NotImplementedError
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def login(self):
        raise NotImplementedError('This feature has not been implemented yet.')

#RuntimeError

#SyntaxError
class User #colon missing so it woould throw a syntax error
    def __init__(self, username, password):
        self.username = username
        self.password = password

#IndentationError

def add_two(x,y):
return x + y

#to escape indentation error
def add_two(x,y):
    pass
return x + y #but this would also be an error as x and y will not defined

#Tab Error

def add_two(x, y):
    return x + y

def pow(n, exp):
  return n**exp

#TypeError

print(5 + 'hi')

#ValueError
int('20.5')

#ImportError
#app.py
import blog
def menu():
    pass

#blog.py
from app import menu

def do_something():
    pass
#in the above case the circular imports causes errors

#DeprecationWarning
from database import Database

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def register(self):
        Database.write(self.username, self.password)
        raise DepricatedWarning('User#register still works but depricated')
    @classmethod
    def register_user(cls, username, password):
        Database.write(username, password)
        return cls(username, password)
        
