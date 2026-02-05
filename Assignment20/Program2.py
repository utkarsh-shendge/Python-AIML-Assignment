#Design a python application that creates two threads named as EvenFactor and OddFactor.

import threading

def EvenFactor(No):
    Sum = 0
    for i in range(2,No,2):
        if (No % i == 0):
            print(i)
            Sum = Sum+i

    print("Sum of Even factors is : ",Sum)

def OddFactor(No):
    Sum = 0
    for i in range(1,No,2):
        if (No % i == 0):
            print(i)
            Sum = Sum+i

    print("Sum of Odd factors is : ",Sum)

def main():
    No = int(input("Enter number : "))

    factEven_t = threading.Thread(target=EvenFactor, args=(No,))

    factOdd_t = threading.Thread(target=OddFactor, args=(No,))


    factOdd_t.start()
    factEven_t.start()

    factOdd_t.join()
    factEven_t.join()

    print("Exit from main")

if __name__ == "__main__":
    main()