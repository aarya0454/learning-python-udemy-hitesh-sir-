class ChaiOrder:
    def __init__(self,type_,size): # this underscore here is used beacause "type" is a sreserved keyword and can't be used directly look into 01class.py
        self.type = type_ # it is same as creating a varibale for the first time 
        self.size = size 
    def summary(self):
        return f'{self.size} ml of {self.type} chai'

order = ChaiOrder("Masala",200) # this is an simple order that creates a new "instance" of the class which takes masala and 200 as a argument which are passed as a parameter 
print(order.summary())


order_two = ChaiOrder("Ginger",220)
print(order_two.summary())
