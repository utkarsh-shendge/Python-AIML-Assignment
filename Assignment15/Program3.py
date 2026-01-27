#Write a lambda function using filter() which accepts a list of numbers and returns a list of odd of numbers.

CheckOdd = lambda No : (No % 2 != 0) 

def main():
    data = []
    n = int(input("Enter the number of elements : "))

    for i in range(n):
        elements = int(input(f"enter element {i+1} : "))
        data.append(elements)

    print(data)

    FData = list(filter(CheckOdd,data))
    print("List of odd numbers : ",FData)

if __name__ == "__main__":
    main()