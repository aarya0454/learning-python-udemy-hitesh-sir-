from functools import wraps
def auth(func):
    wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied : only admin")
            return None
        else:
            return func(user_role)
    return wrapper

@auth
def access(role):
    print("access is granted")

access("admin")
access("user")

def logger(func):
    wraps(func)
    def wrapper(*arg,**kwarg):
        print(f"🚀 function is going to runnnnn !! {func.__name__}")
        result = func(*arg,**kwarg)
        print(f"✅ function executed successfully !! {func.__name__}")
        return result
    return wrapper
@logger
def brew(type, milk="no"):
    print(f"in process {type} and milk status {milk}")

brew("lemon chai")