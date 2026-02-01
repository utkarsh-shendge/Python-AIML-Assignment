#write a program which accept N numbers from user and store it into a list.Return maximum of all
#elements in that list.

def Maximum(Data,N):
    MaxElement = 0
    for i in range(N):
        if MaxElement < Data[i]:
            MaxElement = Data[i]

    return MaxElement

def main():
    Data = []
    N = int(input("Enter number of elements : "))

    for i in range(N):
        Num = int(input(f"Enter {i+1} number : "))
        Data.append(Num)

    Ret = Maximum(Data,N)

    print("Maximum of all elements : ",Ret)    

if __name__ == "__main__":
    main()