#Ben and Dan are two novice software developers. They are trying to build a function that asks 
#user for a number and calculate its power of 2. Here is their first version of code
""" def power_of_two():
    user_input = int(input('Please enter a number: '))
    n = float(user_input)
    n_square = n ** 2
    return(n_square)

print(power_of_two()) """

def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid.')
        n = 0
    else:
        n_square = n ** 2
    finally:
        return n_square
        
sq = power_of_two()
print(sq)

"""
finally:
        n_square = n ** 2
        return n_square #running this will throw errors in the above code
"""