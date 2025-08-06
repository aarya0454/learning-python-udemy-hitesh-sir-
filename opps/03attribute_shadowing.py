class Chai:
    temperature = "hot"
    strength = "strong"


cutting = Chai()
print(cutting.temperature)
cutting.temperature = 'mild'
cutting.cup = "small"
print("after changing", cutting.temperature)
print("cup size is ", cutting.cup)
print("directly look into the class",Chai.temperature)
del cutting.temperature
print(cutting.temperature) # if the refrence of the object attribute is somehow unvailable then it falls back to the value of the class that was defined itself 
del cutting.cup
print("cup size is ", cutting.cup) # because there no fall back if there was this property inside the class then it would have falled back to it but it doesn't there "attribute error  "




# Methods is just a fancy name of the function, if the function is inside the class then it is method else it is a function 
