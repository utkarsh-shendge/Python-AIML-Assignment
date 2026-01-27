#Write a lambda function which accepts one number and returns square of that number.

Square = lambda No : (No ** 2)

def main():
    No = int(input("Enter a number : "))

    Ret = Square(No)
    print(Ret)

if __name__ == "__main__":
    main()