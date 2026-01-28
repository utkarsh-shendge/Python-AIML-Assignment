#Write a program which contains one function named as ChkNum() which accept one parameter as number.
#If number is even then it should display "Even Number" otherwise display "Odd Number" on console.

def ChkNum(No):
    if(No % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    No = int(input("Enter a number : "))
    ChkNum(No)

if __name__ == "__main__":
    main()