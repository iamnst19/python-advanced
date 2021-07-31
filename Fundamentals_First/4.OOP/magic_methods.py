class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self): 
        return len(self.cars)
    def __getitem__(self, i):
        return self.cars[i]
    def __repr__(self): #dunder repr is used to print out a string representing the object
        return f'<Garage {self.cars}>' #this is a garage object and defines it has this list of cars in it
    def __str__(self): #it prints the information of the garage
        return f'Garage with {len(self)} cars.'



ford = Garage()
print(ford.cars) #ford.cars has a property that will be assigned
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford.cars)

#print len of cars.
print(len(ford.cars)) #this uses the dunder len method of the list
#or
print(len(ford)) #in this case the class garage is calling the method __len__ for the obeject ford 

print(ford[0]) #Garage' object is not subscriptable # Garage.__getitem__(ford, 0)

for car in ford: 
    print(car)

print(ford)