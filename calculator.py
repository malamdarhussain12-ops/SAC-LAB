def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b !=0:
        return a/b
    else:
        return "error! division by zero."


print("simple calculator")
a= int(input("enter the first number: "))
b= int(input("enter the second number: "))


print("Addition", add(a,b))
print("Subtraction", subtract(a,b))
print("Multiplication",multiply(a,b))
print("division",divide(a,b))

       
