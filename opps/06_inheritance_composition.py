class BaseChai:
    def __init__(self,type_):
        self.type = type_
    def prepare(self):
        print(f'Preparing {self.type} chai.....')
class MasalaChai(BaseChai): # we only use parenthesis in the name of the class when we want to inherit something in that class and that parenthesis contains the name of the class tyo inherit from 
    def add_spices(self):
        print("Adding cardamon,ginger, cloves.")


class ChaiShop:
    chai_cls = BaseChai # we don't add parenthesis because we are inherting the all values of the "BaseChai" this is a syntax of compostion
    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f'serving {self.chai.type} chai in the shop')
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve() 
fancy.serve()
fancy.chai.add_spices() 