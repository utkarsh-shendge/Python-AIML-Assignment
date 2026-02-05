class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        self.Value1 = int(input("Enter number 1 : "))
        self.Value2 = int(input("Enter number 2 : "))

    def Addition(self):
        return self.Value1+self.Value2
    
    def Subtraction(self):
        return self.Value1-self.Value2
    
    def Multiplication(self):
        return self.Value1*self.Value2
    
    def Division(self):
        try:
            return self.Value1//self.Value2
        except ZeroDivisionError:
            print(ZeroDivisionError)

def main():
    Obj1 = Arithmetic()
    Obj2 = Arithmetic()

    Obj1.Accept()
    print("Addition is : ",Obj1.Addition())
    print("Subtraction is : ",Obj1.Subtraction())
    print("Multiplication is : ",Obj1.Multiplication())
    print("Division is : ",Obj1.Division())

    Obj2.Accept()
    print("Addition is : ",Obj2.Addition())
    print("Subtraction is : ",Obj2.Subtraction())
    print("Multiplication is : ",Obj2.Multiplication())
    print("Division is : ",Obj2.Division())

if __name__ == "__main__":
    main()