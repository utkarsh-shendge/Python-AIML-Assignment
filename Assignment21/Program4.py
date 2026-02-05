#Design a python application that craetes two threads as Thread1 calculates sum of elements in list 
# where Thread2 calculates product of elements in the list.

import threading


def Add(Data):
    Sum = 0
    for i in range(len(Data)):
        Sum = Sum + Data[i]

    print("Product of all elemnts in the list is : ",Sum)

def Mult(Data):   
    mult = 1
    for i in range(len(Data)):
        mult = mult * Data[i]

    print("Sum of all elemnts in the list is : ",mult)

def main():
    N = int(input("Enter number of elements : "))
    Data = []

    for i in range(N):
        No = int(input(f"Enter {i+1} element : "))
        Data.append(No)

    Thread1 = threading.Thread(target=Add, args=(Data,))

    Thread2 = threading.Thread(target=Mult, args=(Data,))
    
    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()