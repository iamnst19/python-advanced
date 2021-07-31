""" class MyCustomError(TypeError):
    pass

raise MyCustomError('Ouch That was error') """

class RuntimeErrorWithCode(TypeError): #multi-line string below the class is called a docstring and it defines what a class does
    """
     Exception raised when a specific error code is needed.
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: message')
        self.code = code


#raise RuntimeErrorWithCode('Ouch That was error', 500)

err = RuntimeErrorWithCode('An error happened', 500)
print(err.__doc__) #this will print out the docstring

print("""
    Hello 
    How are you?
    """)
