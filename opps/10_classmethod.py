class ChaiOrder:
    def __init__(self,tea_type,sweetness,size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
    @classmethod
    def from_dict(cls, order_data): #it doesn't get self it gets "cls" this cls means the class itself therefore the class method gets the whole cls as first parameter but none is given to the static only the one used are given
        return cls( 
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )
    @classmethod
    def from_string(cls,order_string):
        tea_type,sweetness,size = order_string.split("-")
        return cls(tea_type,sweetness,size)
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small","Medium","Large"]

print(ChaiUtils.is_valid_size("Medium"))





order1 = ChaiOrder.from_dict({"tea_type":"masala","sweetness":"medium","size":"large"})
order2 = ChaiOrder.from_string("Ginger-Low-Small")
order3 = ChaiOrder("lemon","no","extra large")
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__) # __dict__ is a dunder that gives the key value pair of the response 
