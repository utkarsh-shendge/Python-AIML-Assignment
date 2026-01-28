#Write a program which accept one number and prints this.
#Input : 5
#Output : 1 
#         1 2
#         1 2 3  
#         1 2 3 4 
#         1 2 3 4 5

def PrintPattern(No):
    J = 0
    for i in range(No):
        print()
        J = J+1
        for j in range(1,J+1):
            print(j,end=" ")

        
def main():
    No = int(input("Enter a number : "))

    PrintPattern(No)

if __name__ == "__main__":
    main()