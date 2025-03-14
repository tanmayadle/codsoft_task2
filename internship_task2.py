# function to perform the arithmetic operation
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y !=0:
        return x/y
    else:
        return "cannot divide by zero!"

#display the menu for the operation

print("select the operation: ")
print("1.add")
print("2,subtract")
print("3.multiply")
print("4.divide")

choice = input("enter choice (1/2/3/4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("enter the second number: "))

#performing the selected operation
if (choice=='1'):
    print(f"{num1}+{num2}={add(num1,num2)}")

elif(choice=='2'):
    print(f"{num1}-{num2}={subtract(num1,num2)}")

elif(choice=='3'):
    print(f"{num1}*{num2}={multiply(num1,num2)}")

elif(choice=='4'):
    print(f"{num1}/{num2}={divide(num1,num2)}")

else:
    print("Invalid input")

    
        
        
