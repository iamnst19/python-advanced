class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects')
        self.cars.append(car)
#        raise NotImplementedError("We can't add cars to garage yet")
"""
ford = Garage()
ford.add_car('Fiesta') #this throws an error as the above as its looking for arguements in Car object
print(len(ford)) """

ford = Garage()
car = Car('Ford', 'Fiesta')
ford.add_car(car) #the value of the car variable is assigned to the parameter(car) in the method add_car

print(len(ford))