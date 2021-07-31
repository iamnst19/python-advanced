class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount: .2f}>'
#   @staticmethod #calling this method allows us call out the method without self as an arguemnet
    """ def from_sum(value1, value2):
        return FixedFloat(value1 + value2) """
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2) #this will allow us to call from the class we define 

#number = FixedFloat(18.5764) 
#new_number = number.from_sum(19.575, 1.89) #FixedFloat(18.5764) is not required here so we use the @staticmethod
new_number = FixedFloat.from_sum(22, 1.999)
print(new_number)  

#creating a class that extends the class
class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'
    
    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount: .2f}>'

#money = Euro(18.76)
money = Euro.from_sum(16.5, 20) #output --> <FixedFloat  36.50> this is returning the first class, what we need is the Euro class, this can be done by changing the @staticmethod to @classmethod
print(money)



