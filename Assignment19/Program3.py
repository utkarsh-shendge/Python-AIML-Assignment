#Write a program which contains filter(), map() and reduce() in it.Python application 
# which contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which greater than or equal to 70 and less than 
# or  equal to 90. Map function will increase each number by 10. Reduce will return product of 
# all that numbers

import functools

def NumFilter(No):
    if (No >= 70 and No <= 90):
        return True
    else:
        return False
    
def NumMap(No):
    return No+10

def Mult(No1,No2):
    return No1*No2


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

    RData = functools.reduce(Mult,MData)

    print("output of reduce : ",RData)


if __name__ == "__main__":
    main()

