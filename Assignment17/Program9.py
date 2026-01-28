#Write a program which accept one number and number of digits in that number.
#Input : 532489
#Output : 6

def CountDigit(No):
    Count = 0
    while(No != 0):
        No = No // 10
        Count = Count+1

    return Count
        
def main():
    No = int(input("Enter a number : "))

    Ret = CountDigit(No)
    print(Ret)

if __name__ == "__main__":
    main()