#Design a python application where multiple threads update a shared variable.

import threading

value = 0
lobj = threading.Lock()

def Increment():
    global value

    for _ in range(10000):
        with lobj:
            value = value+1

def main():
    global value
    
    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)
    t3 = threading.Thread(target=Increment)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Final value is : ",value)

if __name__ == "__main__":
    main()