#Write a program which accepts name from user and displays its length.

def PrintM(name):
    print(len(name))
        
def main():
    name = input("Enter your name : ")

    PrintM(name)

if __name__ == "__main__":
    main()