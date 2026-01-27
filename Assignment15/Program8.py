#Write a lambda function using filter() which accepts a list of numbers and returns the list of numbers divisible by both 3 and 5.

CheckDivisible = lambda No : ((No % 3 == 0) and (No % 5 == 0))

def main():
    data = []
    n = int(input("Enter the number of elements : "))

    for i in range(n):
        elements = int(input(f"enter element {i+1} : "))
        data.append(elements)

    print(data)

    FData = list(filter(CheckDivisible,data))
    print("Numbers divisible by 3 and 5 : ",FData)

if __name__ == "__main__":
    main()