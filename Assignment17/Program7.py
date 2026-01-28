#Write a program which accept one number and prints this.
#Input : 5
#Output : 1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5 
#         1 2 3 4 5
#         1 2 3 4 5

def PrintPattern(No):
    for i in range(No):
        print()
        for j in range(1,No+1):
            print(j,end=" ")

        
def main():
    No = int(input("Enter a number : "))

    PrintPattern(No)

if __name__ == "__main__":
    main()