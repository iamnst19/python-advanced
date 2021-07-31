cars = [
  {'make': 'AUDI', 'model': 'Q2 Dsl', 'mileage': 19896, 'price': 17800}, 
  {'make': 'AUDI', 'model': 'A6 SW Dsl', 'mileage': 87354,'price': 52000},
  {'make': 'SKODA', 'model': 'Fabia', 'mileage': 90613, 'price': 11000},
  {'make': 'AUDI', 'model': 'A4 SW Dsl', 'mileage': 47402, 'price': 93000},
  {'make': 'VOLKSWAGEN', 'model': 'Touran', 'mileage': 28588, 'price': 87000},
  {'make': 'AUDI', 'model': 'A4 Dsl', 'mileage': 66053, 'price': 62000},
]

def calculated_mpg(car): # you can add as many as parameters you want
    mpg = car["mileage"] / car["price"]
    return mpg # here the function ends and none of the code evaluated after this
    
def car_name(car):    
    name = f"{car['make']} {car['model']}"
    return name

def print_car_info(car):   
    name = car_name(car)
    mpg = calculated_mpg(car)
    
    print(f"{name} does {mpg} mpg miles per gallon")

for car in cars:
    mpg = print_car_info(car) # we can call the fuction here without returning as we have already printed it above, printing this will 
 #show the None for name and mpg

 # if the print_Car_info was returned instead of printed then we could have printed in the function call 

#################
# divide 2 numbers
def divide(x,y):
    if y ==0:
        return "You tried to divide by zero"
    else:
        return x / y

ans = divide(6,3)
print(ans)