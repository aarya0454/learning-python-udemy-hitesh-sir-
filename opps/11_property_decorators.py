class TeaLeaf:
    def __init__(self,age):
        self._age=age # a python way of saying that this is an interesting poroperty this hsouldn't be allowed to touch directly there should be a way for reading as well as writing this property 
    @property # this is called as getter 
    def age(self):
        return self._age+2
    @age.setter # this is called is as getter
    def age(self,age):
        if  1<=age<=5:
            self._age = age
        else:
            raise ValueError("Tea leaf age musat be between 1 and 5 yrs")
        
leaf = TeaLeaf(2)
print(leaf.age)
leaf.age = 6
print(leaf.age)