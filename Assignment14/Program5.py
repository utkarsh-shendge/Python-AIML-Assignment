#Write a lambda function which accepts one numbers and returns True if number is even otherwise False.

CheckEven = lambda No : (No % 2 == 0)

def main():
    No = int(input("Enter first number : "))

    Ret = False

    Ret = CheckEven(No)

    print(Ret)

if __name__ == "__main__":
    main()