#write a program which accept N numbers from user and store it into a list. Return addition of all
#  prime numbers from that list. Main python file accepts  N numbers from user and pass each number
# to ChkPrime() function which is part of our user defined module named as MarvellousNum .Name of the 
# function from main python file is ListPrime()

import MarvellousNum

def ListPrime(Data):
    Sum = 0

    for i in range(len(Data)):
        Ret = MarvellousNum.ChkPrime(Data[i])

        if Ret == True:
            Sum = Sum + Data[i]

    return Sum
    

def main():
    Data = []
    N = int(input("Enter number of elements : "))

    for i in range(N):
        Num = int(input(f"Enter {i+1} number : "))
        Data.append(Num)

    Ret = ListPrime(Data)

    print("Addition of all prime numbers is : ",Ret)

if __name__ == "__main__":
    main()