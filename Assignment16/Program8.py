#Write a program which accept number from user and checks whether it is divible 5 and return true if not then false.

def PrintM(No):
    for i in range(No):
        print("*",end=" ")
        
def main():
    No = int(input("Enter a number: "))

    PrintM(No)

if __name__ == "__main__":
    main()