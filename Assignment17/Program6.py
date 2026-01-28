#Write a program which accept one number and prints this.
#Input : 5
#Output : * * * * *
#         * * * *
#         * * *
#         * * 
#         *

def PrintPattern(No):
    J = No+1
    for i in range(No):
        print()
        J = J-1
        for j in range(J):
            print("*",end=" ")

        
def main():
    No = int(input("Enter a number : "))

    PrintPattern(No)

if __name__ == "__main__":
    main()