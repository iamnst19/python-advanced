
class Movie:
    def __init__(self, name_movie, name_director):
        self.name = name_movie 
        self.director = name_director
    def print_info(self):
        print(f"<<{self.name}>> by {self.director}")

my_movie = Movie('The Matrix', 'Wachowski')
print((my_movie.name))
my_movie.print_info()