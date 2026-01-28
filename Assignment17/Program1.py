#Create a module named as ArithmaticModule which contains 4 functions as Add() for addition, Sub() for subtraction,
#  Mult() for multiplication, Div() for division. All functions should accept two parameters as number and perform operation.Write one 
# python program which call the functions from Arithmatic module by accepting the parameters from user.

import ArithmaticModule

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = 0

    Ret = ArithmaticModule.Add(No1,No2)
    print("Addition is : ",Ret)

    Ret = ArithmaticModule.Sub(No1,No2)
    print("Subtraction is : ",Ret)

    Ret = ArithmaticModule.Mult(No1,No2)
    print("Multiplication is : ",Ret)

    Ret = ArithmaticModule.Div(No1,No2)
    print("Division is : ",Ret)

if __name__ == "__main__":
    main()