#Write a lambda function using reduce() which accepts a list of numbers and returns the product of all numbers.

from functools import reduce

MultNum = lambda A,B : A*B

def main():
    data = []
    n = int(input("Enter the number of elements : "))

    for i in range(n):
        elements = int(input(f"enter element {i+1} : "))
        data.append(elements)

    print(data)

    FData = reduce(MultNum,data)
    print("Product of all numbers is : ",FData)

if __name__ == "__main__":
    main()