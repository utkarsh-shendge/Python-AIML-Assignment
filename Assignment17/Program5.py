#Write a program which accept one number and check whether number is prime or not.

def CheckPrime(No):
    for i in range(2,No):
        if(No % i != 0):
            return True
        else:
            return False
        
def main():
    No = int(input("Enter a number : "))
    Ret = 0

    Ret = CheckPrime(No)
    
    if (Ret == True):
        print("It is prime number")
    else:
        print("It is not prime number")

if __name__ == "__main__":
    main()