#Write a python program to implement a class method named BankAccount.

class BankAccount:
    ROI = 10.5

    def __init__(self,AName,ABalance):
        self.Name = AName
        self.Amount = ABalance
        
    def Display(self):
        print("Account Holder Name : ",self.Name)
        print("Account Balance : ",self.Amount)

    def Deposit(self,DepoAmount):
        self.Amount += DepoAmount
        print(DepoAmount,"deposited sucessfully")

    def Withdraw(self,WithAmount):
        if (WithAmount <= self.Amount):
            self.Amount -= WithAmount
            print(WithAmount,"withdrawl sucessfully")
        else:
            print("Insufficient amount")

    def CalculateInterest(self):
        Interest = (self.Amount * self.ROI) / 100
        return Interest

def main():
    Obj1 = BankAccount("Utkarsh",1000)
    Obj1.Display()
    Obj1.Deposit(1000)
    Obj1.Display()
    Obj1.Withdraw(500)
    Obj1.Display()
    print(Obj1.CalculateInterest())

if __name__ == "__main__":
    main()