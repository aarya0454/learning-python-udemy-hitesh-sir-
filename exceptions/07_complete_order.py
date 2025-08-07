class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala":20, "ginger":40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not available")
        if not isinstance(cups,int):
            raise TypeError("Number of cups should be integer")
        total = menu[flavor] * cups
        print(f' Your bill for {cups} cups of {flavor} chai: ruppes {total}')
    except Exception as e:
        print("error",e)
    finally:
        print("Thank you for visiting chaicode!")


bill("mint",2)
bill("masala","two")
bill("masala",2)