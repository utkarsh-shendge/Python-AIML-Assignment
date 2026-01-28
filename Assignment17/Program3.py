#Write a program which accept one number and returns its factorial.

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    No = int(input("Enter a number : "))
    Ret = 0

    Ret = Factorial(No)
    print("Facorial is : ",Ret)

if __name__ == "__main__":
    main()