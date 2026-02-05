#Design a python application that creates two threads named Prime and Non Prime.

import threading

def Prime(Data):
    print("Prime numbers : ")
    for i in range(len(Data)):
        for j in range(2,Data[i]):
            if (Data[i] % j == 0):
                break
        else:
            print(Data[i],end=" ")
    print()

def NonPrime(Data):
    print("Non prime numbers : ")
    for i in range(len(Data)):
        for j in range(2,Data[i]):
            if Data[i] % j == 0:
                print(Data[i],end=" ")
                break
    print()

def main():
    N = int(input("Enter number of elements : "))
    Data = []

    for i in range(N):
        No = int(input(f"Enter {i+1} number : "))
        Data.append(No)

    Prime_t = threading.Thread(target=Prime, args=(Data,))

    NonPrime_t = threading.Thread(target=NonPrime, args=(Data,))

    Prime_t.start()
    Prime_t.join()

    NonPrime_t.start()
    NonPrime_t.join()

if __name__ == "__main__":
    main()