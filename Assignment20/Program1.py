#Design a python application that creates two seperate threads named as Even and Odd.

import threading

def DisplayEven():
    print("Even : ")
    for i in range(2,21,2):
        print(i)

def DisplayOdd():
    print("Odd : ")
    for i in range(1,20,2):
        print(i)

def main():

    even_t = threading.Thread(target=DisplayEven)

    odd_t = threading.Thread(target=DisplayOdd)

    even_t.start()
    odd_t.start()

    even_t.join()
    odd_t.join()

if __name__ == "__main__":
    main()