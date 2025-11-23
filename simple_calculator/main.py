# Write a program that functions as a simple calculator.
# The program should take two numbers and an operator (+, -, *, /) as input
# and output the result of the operation.


def calculator(num1, num2, operator):
    try:
        match operator:
            case "+":
                print(f"Addition : {num1 + num2}")
                print("======================")

            case "-":
                print(f"Subtraction : {num1 - num2}")
                print("======================")

            case "*":
                print(f"Multiplication : {num1 * num2}")
                print("======================")

            case "/":
                print(f"Division : {num1 / num2}")
                print("======================")

            case _:
                print("Invalid operator!")
                print("======================")
            
            

    except ZeroDivisionError:
        print("Denominator should not be zero.")
        print("======================")


# ----------------------------
# SAFE INPUT HANDLING
# ----------------------------
while True:
    print("\n--- Simple Calculator ---")
    try:
        
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        print()
        print("Enter + for Addition\nEnter - for Subtraction\nEnter * for multiplication\nEnter / for division")
        print()

        operator = input("Enter operator : ")
        print("======================")


        calculator(num1, num2, operator)

    except ValueError:
        print("Invalid input! Only numbers are allowed.")
        print()




    
