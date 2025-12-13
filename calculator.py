import math

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error : Cannot divide by zero!"

def power(a, b):
    return a**b

def square_root(a):
    if a >= 0:
        return math.sqrt(a)

    else:
        return "The number is negative give it in positive please."
    
def percentage(a, b):
    return (a/100)*b 
       
def calculator():
    print("---------------------------------------------")
    print(".....Simple Calculator made with python.....")
    print("---------------------------------------------") 

    while True:
        print("\nChoose Operation  :")
        print("1. Addition")
        print("2. Subtract")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Percentage")
        print("8. Exit Calculator")

        choice = input("Enter choice (1-8) :")

        if choice=="8":
            print("Exiting Calculator. Goodbye !!!")
            break
        
        if choice not in ["1","2","3","4","5","6","7"]:
            print("Invalid choice please try again !!!")
            continue
        
        if choice == "6":
            a = float(input("Enter number : "))
            result = square_root(a)
            print(f"The square root of {a} is {result}")

        else:    
            try:
                num1 = float(input("Enter first number :"))
                num2 = float(input("Enter second number :"))
            except ValueError:
                print("Invalid input please enter number only.")
                continue

        if choice=="1":
            result = add(num1, num2)
            print(f"Result : {result}")

        elif choice=="2":
            result = subtract(num1, num2)
            print(f"Result : {result}")

        elif choice=="3":
            result = multiply(num1, num2) 
            print(f"Result : {result}")

        elif choice=="4":
            result = divide(num1, num2)
            print(f"Result : {result}")
        
        elif choice=="5":
            result = power(num1, num2)
            print(f"{num1}^{num2} = {result}")
        
        elif choice=="7":
            result = percentage(num1, num2)
            print(f"{num1} % of {num2} = {result}")
        
if __name__ == "__main__":
    calculator()  