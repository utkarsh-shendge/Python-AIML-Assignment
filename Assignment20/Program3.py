#Design a python application that creates two threads named as EvenList and OddList.

import threading

def EvenList(Data):
    Sum = 0
    for i in range(len(Data)):
        if (Data[i] % 2 == 0):
            print(Data[i])
            Sum = Sum + Data[i]

    print("Sum of Even elements is : ",Sum)

def OddList(Data):
    Sum = 0
    for i in range(len(Data)):
        if (Data[i] % 2 != 0):
            print(Data[i])
            Sum = Sum + Data[i]

    print("Sum of Odd elements is : ",Sum)

def main():
    No = int(input("Enter number of elements : "))
    Data = []

    for i in range(No):
        Num = int(input(f"Enter {i+1} number : "))
        Data.append(Num)

    factEven_t = threading.Thread(target=EvenList, args=(Data,))

    factOdd_t = threading.Thread(target=OddList, args=(Data,))


    factOdd_t.start()
    factEven_t.start()

    factOdd_t.join()
    factEven_t.join()

    print("Exit from main")

if __name__ == "__main__":
    main()