class Demo:
    Value = 0

    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B

    def Fun(self):
        print("Instance variables from Fun No1 and No2 are : ",self.No1,self.No2)

    def Gun(self):
        print("Instance variables from Gun No1 and No2 are : ",self.No1,self.No2)

def main():
    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()

    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()