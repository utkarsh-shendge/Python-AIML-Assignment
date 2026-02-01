#write a program which accept N numbers from user and store it into a list.Accept one another
# number and returns frequency of that number.

def Frequency(Data,N,No):
    Count = 0
    for i in range(len(Data)):
        if Data[i] == No:
            Count = Count+1

    return Count

def main():
    Data = []
    N = int(input("Enter number of elements : "))

    for i in range(N):
        Num = int(input(f"Enter {i+1} number : "))
        Data.append(Num)

    No = int(input("Enter number to check freq. : "))

    Ret = Frequency(Data,N,No)

    print(f"Frequency of {No} : ",Ret)    

if __name__ == "__main__":
    main()