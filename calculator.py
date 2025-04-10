def add(a,b):
    # add two numbers and return the result
    return a + b
def substract(a,b):
    # substract b from a and return the result
    return a - b

# test our functions
print(f"5 +3 = {add(5, 3)}")
print(f"10 - 4 = {substract(10,4)}")

def multiply(a, b):
    # multiply two numbers and return the result
    return a * b
# test new function
print(f"4 * 6 = {multiply(4, 6)}")
def divide(a, b):
    # divide a by b and return the result.Returns error message if b is zero.
    return a / b if b !=0 else "Error: Division by zero"

    #test the new function
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"5 / 0 = {divide(5 , 0)}")
