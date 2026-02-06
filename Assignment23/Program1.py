#Write a python program to implement a class method named BookStore.

class BookStore:
    NoOfBooks = 0

    def __init__(self,BName,BAuthor):
        self.Name = BName
        self.Author = BAuthor
        self.NoOfBooks += 1
        
    def Display(self):
        print(self.Name,"by",self.Author,".No of books : ",self.NoOfBooks)

def main():
    Obj1 = BookStore("Linux System Programming","Robert Love")
    Obj1.Display()

    Obj2 = BookStore("C Programming","Dennis Ritchie")
    Obj2.Display()

if __name__ == "__main__":
    main()