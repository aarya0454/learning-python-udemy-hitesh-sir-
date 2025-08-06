class Chaicup:
    size= 150 #ml
    def describe(self):# if it were not inside the class then it would have
    #been a function
    #but as it is inside the class then it is a method and 
     #the first thing which is passed in the method is "self"
        return f'A {self.size}ml chai cup'


cup  = Chaicup()
print(cup.describe())
print(Chaicup.describe(Chaicup)) # here the positional argument tells the method describe who's calling you is it Chaicup or cup or who !!
cup_two = Chaicup()
print(cup_two.describe())