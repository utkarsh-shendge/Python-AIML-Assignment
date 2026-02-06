#Write a python program to implement a class named as Numbers.

class Numbers : 
    Sum = 0
    def __init__(self,No):
        self.Value = No
        print("Input : ",No)

    def ChkPrime(self):
        print("Prime Number: ",end=" ")
        for i in range(2,self.Value):
            if (self.Value % i == 0):
                return False
            else:
                return True
            
    def ChkPerfect(self):
        print("Perfect Number : ",end=" ")
        for i in range(1,self.Value):
            if self.Value % i == 0:
                self.Sum = self.Sum + i

        if self.Sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        print("Factors are : ")
        for i in range(1,self.Value):
            if self.Value % i == 0:
                print(i,end=" ")
        print( )

    def SumFactors(self):
        print("Sum of factors is : ",self.Sum)

def main():
    Obj1 = Numbers(6)
    print(Obj1.ChkPrime())
    print(Obj1.ChkPerfect())
    Obj1.Factors()
    Obj1.SumFactors()

if __name__ == "__main__":
    main()