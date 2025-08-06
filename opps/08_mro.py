class A:
    label = "A:Base class"
class B(A):
    label = "B:Masala blend"
class C(A):
    label = "C: herbel blend"
class D(C,B):# whichever class is written first will be called 
    pass
cup = D()
print(cup.label)
print(D.__mro__)