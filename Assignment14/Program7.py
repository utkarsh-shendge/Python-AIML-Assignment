#Write a lambda function which accepts one number and returns True if divisible by 5.

CheckDivisible = lambda No : (No % 5 == 0)

def main():
    No = int(input("Enter first number : "))

    Ret = False

    Ret = CheckDivisible(No)

    print(Ret)

if __name__ == "__main__":
    main()