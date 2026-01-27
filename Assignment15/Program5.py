#Write a lambda function using reduce() which accepts a list of numbers and returns the maximum of all numbers.

from functools import reduce

Maximum = lambda A,B : (A if (A > B) else B)

def main():
    data = []
    n = int(input("Enter the number of elements : "))

    for i in range(n):
        elements = int(input(f"enter element {i+1} : "))
        data.append(elements)

    print(data)

    FData = reduce(Maximum,data)
    print("Maximum number is : ",FData)

if __name__ == "__main__":
    main()