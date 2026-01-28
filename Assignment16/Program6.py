#Write a program which accept number from user and checks whether it is positive, negative or zero.

def CheckInt(No):
    if (No == 0):
        print("Zero")
    elif (No > 0):
        print("Positive")
    elif (No < 0):
        print("Negative")

def main():
    No = int(input("Enter a number: "))

    CheckInt(No)

if __name__ == "__main__":
    main()