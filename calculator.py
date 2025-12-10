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
        print("5. Exit Calculator")

        choice = input("Enter choice (1-5) :")

        if choice=="5":
            print("Exiting Calculator. Goodbye !!!")
            break
        
        if choice not in ["1","2","3","4"]:
            print("Invalid choice please try again !!!")
            continue

        try:
            num1 = float(input("Enter first number :"))
            num2 = float(input("Enter second number :"))
        except ValueError:
            print("Invalid input please anter number only.")

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

if __name__ == "__main__":
    calculator()  
