#Write a program which accept one number and returns addition of digits in that number.
#Input : 532489
#Output : 6

def AddDigit(No):
    Rem = 0
    Sum = 0
    while(No != 0):
        Rem = No % 10
        No = No // 10
        Sum = Sum + Rem

    return Sum
        
def main():
    No = int(input("Enter a number : "))

    Ret = AddDigit(No)
    print(Ret)

if __name__ == "__main__":
    main()