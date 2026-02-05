#Design a python application that creates two threads named Prime and Non Prime.

import threading

def Maximum(Data):
    print("Maximum is : ")
    MaxNum = 0
    for i in range(len(Data)):
        if Data[i] > MaxNum:
            MaxNum = Data[i]

    print(MaxNum)

def Minimum(Data):
    print("Minimum is : ")
    MinNum = Data[1]
    for i in range(len(Data)):
        if Data[i] < MinNum:
            MinNum = Data[i]

    print(MinNum)

def main():
    N = int(input("Enter number of elements : "))
    Data = []

    for i in range(N):
        No = int(input(f"Enter {i+1} number : "))
        Data.append(No)

    Max_t = threading.Thread(target=Maximum, args=(Data,))

    Min_t = threading.Thread(target=Minimum, args=(Data,))

    Max_t.start()
    Max_t.join()

    Min_t.start()
    Min_t.join()

if __name__ == "__main__":
    main()