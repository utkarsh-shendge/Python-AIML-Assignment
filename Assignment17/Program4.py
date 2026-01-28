#Write a program which accept one number and returns addition of its factors.

def AddFact(No):
    Fact = 0

    for i in range(1,No):
        if (No % i == 0):
            Fact = Fact + i

    return Fact

def main():
    No = int(input("Enter a number : "))
    Ret = 0

    Ret = AddFact(No)
    print("Addition of factors is : ",Ret)

if __name__ == "__main__":
    main()