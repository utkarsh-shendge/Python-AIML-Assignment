#Write a lambda function using filter() which accepts a list of strings and returns the list of strings length greater than 5.

StrLength = lambda A : (A if(len(A) > 5) else None)

def main():
    data = []
    n = int(input("Enter the number of elements : "))

    for i in range(n):
        elements = input(f"enter element {i+1} : ")
        data.append(elements)

    print(data)

    FData = list(filter(StrLength,data))
    print("String length greater than 5 : ",FData)

if __name__ == "__main__":
    main()