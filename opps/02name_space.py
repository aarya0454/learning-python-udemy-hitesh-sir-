class Chai:
    origin ="India" #inside the class whenever the variable goes we call it properties 
print(Chai.origin)
Chai.is_hot = True # this "is_hot" is called attribute normally it is called variable but inside the class it is called attribute 
print(Chai.is_hot)
# creating objects from class Chai
masala = Chai()
print(f" Masala {masala.origin}")
print(f" Masala {masala.is_hot}")
masala.is_hot = False

print(f'Chai {Chai.is_hot}')
print(f'masala {masala.is_hot}')
# each object has it's own name space that doesn't affect(doesn't change any value of) other objects or class by default 
masala.flavor = "Masala"
print(masala.flavor)