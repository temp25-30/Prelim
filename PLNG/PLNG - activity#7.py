#ARITHMETIC PROGRAM
def inputCatch(callerFunc, divOp):
    if divOp == True:
        try:
            uNum = int(input())
            return uNum
        except ValueError:
            print("ERROR! That was not a valid number!")
            callerFunc()
        except ZeroDivisionError:
            print("ERROR! You cannot use 0 for division operation!")
            callerFunc()
    else:
        try:
            uNum = int(input())
            return uNum
        except ValueError:
            print("ERROR! That was not a valid number!")
            callerFunc()

def addition():
    print("Enter the value of x:")
    x = inputCatch(addition, False)
    print("Enter the value of y:")
    y = inputCatch(addition, False)

    print(f"Variable Values: x = {x}, y = {y}")
    result = x + y + 0.0
    print("Addition: x + y =", result)

def subtraction():
    print("Enter the value of x:")
    x = inputCatch(subtraction,False)
    print("Enter the value of y:")
    y = inputCatch(subtraction,False)

    print(f"Variable Values: x = {x}, y = {y}")
    result = x - y + 0.0
    print("Subtraction: x - y =",result)

def Multiplication():
    print("Enter the value of x:")
    x = inputCatch(Multiplication,False)
    print("Enter the value of y:")
    y = inputCatch(Multiplication,False)

    print(f"Variable Values: x = {x}, y = {y}")
    result = x * y + 0.0
    print("Multiplication: x * y =",result)

def Division():
    print("Enter the value of x:")
    x = inputCatch(Division,True)
    print("Enter the value of y:")
    y = inputCatch(Division,True)

    if y == 0 or x == 0:
        print("0 is not allowed for division operation.")
        Division()
    else:
        print(f"Variable Values: x = {x}, y = {y}")
        result = x / y
        print("Division: x / y =",result)

def Modulus():
    print("Enter the value of x:")
    x = inputCatch(Modulus,True)
    print("Enter the value of y:")
    y = inputCatch(Modulus,True)

    if y == 0 or x == 0:
        print("0 is not allowed for modulo division operation.")
        Modulus()
    else:
        print(f"Variable Values: x = {x}, y = {y}")
        result = x % y
        print("Modulus: x % y =",result)

def incre():
    print("Enter the value of x:")
    x = inputCatch(incre,False)
    x += 1
    print("Variable Value:",x-1,"Incremented =",x)

def decre():
    print("Enter the value of x:")
    x = inputCatch(decre,False)
    x -= 1
    print("Variable Value:",x+1,"Decremented =",x)

def main():
    print("ARITHMETIC CALCULATOR\n 1. Addition\t2. Subtraction\t3. Multiplication\n4. Division\t5. Modulus\t6. Increment\n7. Decrement\n")
    print("Select an arithmetic operation (Only input the number): ")
    choice = inputCatch(main,False)

    match choice:
        case 1:
            addition()
        case 2:
            subtraction()
        case 3:
            Multiplication()
        case 4:
            Division()
        case 5:
            Modulus()
        case 6:
            incre()
        case 7:
            decre()
        case _:
            print("Please enter a valid option.")
            main()

    print("Do you want to continue? (YES/NO):")
    contAns = input()

    if contAns.lower() == "no":
        print("Program terminated. Thank you!")
    elif contAns.lower() == "yes":
        main()
    else:
        print("Please enter either YES or NO only.")
        print("Do you want to continue? (YES/NO):")
        contAns = input()

if __name__ == "__main__":
    main()
