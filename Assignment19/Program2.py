#Write a program which contains one lamda function which accepts one parameter and return power of two.

Mult = lambda No1,No2 : No1*No2

def main():
    No1 = int(input("Enter number : "))
    No2 = int(input("Enter number : "))

    Ret = 0

    Ret = Mult(No1,No2)

    print(Ret)

if __name__ == "__main__":
    main()

