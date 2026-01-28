#Write a program which accept one number and display below pattern
#Input:     5
#Output:     *   *   *   *   *
#            *   *   *   *   *
#            *   *   *   *   *
#            *   *   *   *   *
#            *   *   *   *   *

def PrintPattern(No):
    for i in range(No):
        print()
        for j in range(No):
            print("*",end=" ")

def main():
    No = int(input("Enter a number : "))

    PrintPattern(No)

if __name__ == "__main__":
    main()