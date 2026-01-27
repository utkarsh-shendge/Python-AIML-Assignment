#Write a lambda function using filter() which accepts a list of numbers and returns a list of even of numbers.

CheckEven = lambda No : (No % 2 == 0) 

def main():
    data = []
    n = int(input("Enter the number of elements : "))

    for i in range(n):
        elements = int(input(f"enter element {i+1} : "))
        data.append(elements)

    print(data)

    FData = list(filter(CheckEven,data))
    print("List of even numbers : ",FData)

if __name__ == "__main__":
    main()