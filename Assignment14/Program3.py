#Write a lambda function which accepts two numbers and returns maximum number.

Maximum = lambda No1,No2 : (No1 > No2)

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = False

    Ret = Maximum(No1,No2)

    if Ret == True : 
        print(No1)
    else:
        print(No2)

if __name__ == "__main__":
    main()