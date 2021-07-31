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

ford = Garage()

fiesta = Car('Ford', 'Fiesta')

#print(len(ford))

try:
    ford.add_car(fiesta)
except TypeError:
    print("Your car was not a car")
except ValueError:
    print('Something weird just happened') #when handling multiple errors

finally:
    print(f"The garage now has {len(ford)} cars!!")

""" if isinstance(fiesta, Car):
    ford.add_car(fiesta)
  
else:
    print("Your car was not a Car!") """