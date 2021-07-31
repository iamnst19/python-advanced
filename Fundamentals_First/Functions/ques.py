""" What would the output of this segment of code be?

It's a tricky one! Notice that the lambda function is defined inside the last line. """

def over_age(data, getter):
    return getter(data) >= 18
 
user = { 'username': 'rolf123', 'age': '35' }
 
print(over_age(user, lambda x: int(x['age'])))