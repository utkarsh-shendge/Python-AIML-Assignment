#Write a program which contains filter(), map() and reduce() in it.Python application 
# which contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which are prime. Map function will multiply each number by2. 
# Reduce will return maximum of all that numbers

import functools

def NumFilter(No):
    for i in range(2,No):
        if (No % i != 0):
            return True
        else:
            return False
    
def NumMap(No):
    return No*2

def Maximum(No1,No2):
    if No1>No2:
        return No1
    else:
        return No2


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

    RData = functools.reduce(Maximum,MData)

    print("output of reduce : ",RData)


if __name__ == "__main__":
    main()

