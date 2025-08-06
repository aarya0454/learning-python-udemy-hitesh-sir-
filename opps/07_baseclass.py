class Chai:
    def __init__(self,type_,strength):
        self.type = type_
        self.strength = strength

# class GingerChai(Chai):
#     def __init__(self, type_, strength):
#         def __init__(type_, strength,spice_level):
#             self.type = type_
#             self.strength = strength
#             self.spice_level = spice_level

# class GingerChai(Chai):
#     def __init__(self, type_, strength,spice_level):
#         Chai.__init__(self,type_,strength)
#         self.spice_level = spice_level.    # this whole method is known as explicit method to access the base class 

class GingerChai(Chai):
    def __init__(self, type_, strength,spice_level):
        super().__init__(type_, strength) # this method is known as the super() method to access the base class 
        self.spice_level = spice_level