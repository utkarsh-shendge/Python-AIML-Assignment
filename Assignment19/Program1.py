#Write a program which contains one lamda function which accepts one parameter and return power of two.

Power = lambda No : No*No

def main():
    No = int(input("Enter number : "))
    Ret = 0

    Ret = Power(No)

    print(Ret)

if __name__ == "__main__":
    main()

