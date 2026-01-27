#Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

CheckSquare = lambda No : No*No

def main():
    data = []
    n = int(input("Enter the number of elements : "))

    for i in range(n):
        elements = int(input(f"enter element {i+1} : "))
        data.append(elements)

    print(data)

    MData = list(map(CheckSquare,data))
    print("List of square of numbers : ",MData)

if __name__ == "__main__":
    main()