#Design a python application that creates three threads named as Thread1 and Thread2.

import threading

def printNormal():
    for i in range(1,51):
        print(i)

    print("Thread1 completed")
    
def printReverse():
    for i in range(50,0,-1):
        print(i)

    print("Thread2 completed")

def main():
    Thread1 = threading.Thread(target=printNormal)

    Thread2 = threading.Thread(target=printReverse)

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()