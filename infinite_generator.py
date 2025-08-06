def infinit_gen():
    print("Hi! what chai would you like to have")
    order = yield
    while True:
        print(f"your {order} is being prepared")
        order = yield

chai = infinit_gen()
next(chai)
chai.send("masala chai")
chai.send("Lemon Tea")
def token_dispenser(start: int = 1): 
    try:
        while True:
            received = yield start
            if received is not None :
                start =  received
            else:
                start = start+1 
    except:
        print("Dispenser closed")