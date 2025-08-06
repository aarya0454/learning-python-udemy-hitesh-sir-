
counter= 0
def impure_increment():
    global counter
    counter+= 1
    return counter
def factorial_recursive(n):
    if n<=1:
        return 1 
    else:
        fact = n*factorial_recursive(n-1)
        return fact
def square_list(nums):
    final = map(lambda x: x**2, nums)
    return list(final)
print(square_list([1, 4, 9]))