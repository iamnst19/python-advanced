#Here we are taking the dictionary outside of the function and placing it her 
car = {
    "make": "Ford",
    "model": "Fiests",
    "mileage": 23000,
    "fuel_consumed": 460
}

def calculated_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"]/car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} mpg miles per gallon")

# value you pass into the function is called ARGUEMENT and 
# the variable that accepts a value inside the function is called PARAMETER

calculated_mpg({
    "make": "Ford",
    "model": "Fiests",
    "mileage": 23000,
    "fuel_consumed": 460
})
####################################
cars = [
  {'make': 'AUDI', 'model': 'Q2 Dsl', 'mileage': 19896, 'price': 17800}, 
  {'make': 'AUDI', 'model': 'A6 SW Dsl', 'mileage': 87354,'price': 52000},
  {'make': 'SKODA', 'model': 'Fabia', 'mileage': 90613, 'price': 11000},
  {'make': 'AUDI', 'model': 'A4 SW Dsl', 'mileage': 47402, 'price': 93000},
  {'make': 'VOLKSWAGEN', 'model': 'Touran', 'mileage': 28588, 'price': 87000},
  {'make': 'AUDI', 'model': 'A4 Dsl', 'mileage': 66053, 'price': 62000},
]

def calculated_mpg(car_to_calculate, intro): # you can add as many as parameters you want
    print(intro)
    mpg = car_to_calculate["mileage"] / car_to_calculate["price"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} mpg miles per gallon")

calculated_mpg(cars[1], "Hey Car")
for car in cars:
    calculated_mpg(car, "Car Here")