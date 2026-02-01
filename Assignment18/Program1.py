#write a program which accept N numbers from user and store it into a list.Return addition of all
#elements in that list.

def Add(Data,N):
    Sum = 0
    for i in range(N):
        Sum = Sum + Data[i]

    return Sum

def main():
    Data = []
    N = int(input("Enter number of elements : "))

    for i in range(N):
        Num = int(input(f"Enter {i+1} number : "))
        Data.append(Num)

    Ret = Add(Data,N)

    print("Addition of all elements : ",Ret)    

if __name__ == "__main__":
    main()