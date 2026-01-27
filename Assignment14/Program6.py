#Write a lambda function which accepts one number and returns True if number is odd otherwise False.

CheckOdd = lambda No : (No % 2 != 0)

def main():
    No = int(input("Enter first number : "))

    Ret = False

    Ret = CheckOdd(No)

    print(Ret)

if __name__ == "__main__":
    main()