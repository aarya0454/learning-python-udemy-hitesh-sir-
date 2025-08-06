class Chai:
    pass


class ChaiTime:
    pass

print(type(Chai)) # class type but everything in python is object !
ginger_tea = Chai()
print(type(ginger_tea))
print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)
# Each object has it's entity it doesn't bother other entities of the class that is known as name space 


