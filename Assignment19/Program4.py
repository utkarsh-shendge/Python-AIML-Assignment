#Write a program which contains filter(), map() and reduce() in it.Python application 
# which contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which are even. Map function will calculate its square. 
# Reduce will return addition of all that numbers

import functools

def NumFilter(No):
    if (No % 2 == 0):
        return True
    else:
        return False
    
def NumMap(No):
    return No*No

def Add(No1,No2):
    return No1+No2


def main():
    N = int(input("Enter number of elements : "))
    Data = []

    for i in range(N):
        No = int(input(f"Enter {i+1} element : "))
        Data.append(No)

    print("Input list : ",Data)
    
    FData = list(filter(NumFilter,Data))

    print("List after filter : ",FData)

    MData = list(map(NumMap,FData))

    print("List after map : ",MData)

    RData = functools.reduce(Add,MData)

    print("output of reduce : ",RData)


if __name__ == "__main__":
    main()

