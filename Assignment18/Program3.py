#write a program which accept N numbers from user and store it into a list.Return maximum of all
#elements in that list.

def Minimum(Data,N):
    MinElement = Data[0]
    for i in range(N):
        if MinElement > Data[i]:
            MinElement = Data[i]

    return MinElement

def main():
    Data = []
    N = int(input("Enter number of elements : "))

    for i in range(N):
        Num = int(input(f"Enter {i+1} number : "))
        Data.append(Num)

    Ret = Minimum(Data,N)

    print("Minimum of all elements : ",Ret)    

if __name__ == "__main__":
    main()