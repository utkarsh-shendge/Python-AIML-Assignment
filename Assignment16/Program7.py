#Write a program which accept number from user and checks whether it is divible 5 and return true if not then false.

def CheckDiv(No):
    if (No % 5 == 0):
        return True
    else:
        return False

def main():
    No = int(input("Enter a number: "))
    Ret = False

    Ret = CheckDiv(No)
    print(Ret)

if __name__ == "__main__":
    main()