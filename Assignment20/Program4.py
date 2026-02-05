#Design a python application that creates three threads named as Capital, Small and Digits.

import threading

def printCapital(inp):
    Count = 0

    for i in inp:
        if (i >= 'A' and i <= 'Z'):
            Count = Count+1
    print("Thread ID : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)
    print("Capital characters : ",Count)
    print()

def printSmall(inp):
    Count = 0

    for i in inp:
        if (i >= 'a' and i <= 'z'):
            Count = Count+1
    print("Thread ID : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)
    print("Small characters : ",Count)
    print()

def printDigit(inp):
    Count = 0

    for i in inp:
        if (i >= '0' and i <= '9'):
            Count = Count+1
    print("Thread ID : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)
    print("Digit characters : ",Count)
    print()

def main():
    inp = input("Enter input : ")

    Capital_t = threading.Thread(target=printCapital, args=(inp,), name="Capital")

    Small_t = threading.Thread(target=printSmall, args=(inp,), name="Small")

    Digit_t = threading.Thread(target=printDigit, args=(inp,), name="Digits")


    Capital_t.start()
    Small_t.start()
    Digit_t.start()
    
    Capital_t.join()
    Small_t.join()
    Digit_t.join()

    print("Exit from main")

if __name__ == "__main__":
    main()