# def display_menu():
#     print("\nWelcome to the Data Analyzer and Transformer Program")
#     print("\nMain Menu:")
#     print("1. Input Data")
#     print("2. Display Data Summary ")
#     print("3. Calculate Factorial ")
#     print("4. Filter Data by Threshold ")
#     print("5. Sort Data")
#     print("6. Display Dataset Statistics ")
#     print("7. Exit Program")

# def input_data():
#     global data
#     raw_input = input("\nStep 1: Input Data\nEnter data for a 1D array : ")
#     data = list(map(int, raw_input.strip().split()))
#     print("\nData has been stored successfully!")

# def data_summary():
#     if not data:
#         print("No data found. Please input data first.")
#         return
#     print("\nData Summary:")
#     print(f"Total elements: {len(data)}")
#     print(f"Minimum value: {min(data)}")
#     print(f"Maximum value: {max(data)}")
#     print(f"Sum of all values: {sum(data)}")
#     print(f"Average value: {round(sum(data)/len(data), 2)}")

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# def calculate_factorial():
#     num = int(input("\nEnter a number to calculate its factorial: "))
#     result = factorial(num)
#     print(f"\nFactorial of {num} is: {result}")

# def filter_data_by_threshold():
#     if not data:
#         print("No data found. Please input data first.")
#         return
#     threshold = int(input("\nEnter a threshold value to filter out data above this value: "))
#     filtered = list(filter(lambda x: x >= threshold, data))
#     print("\nFiltered Data (values >= {}): {}".format(threshold, ", ".join(map(str, filtered))))

# def sort_data():
#     if not data:
#         print("No data found. Please input data first.")
#         return
#     print("\nChoose sorting option:\n1. Ascending\n2. Descending")
#     choice = input("Enter your choice: ")
#     sorted_data = sorted(data) if choice == '1' else sorted(data, reverse=True)
#     order = "Ascending" if choice == '1' else "Descending"
#     print(f"\nSorted Data in {order} Order: {', '.join(map(str, sorted_data))}")

# def get_statistics(data_list):
#     minimum = min(data_list)
#     maximum = max(data_list)
#     total = sum(data_list)
#     average = round(total / len(data_list), 2)
#     return minimum, maximum, total, average

# def display_statistics():
#     if not data:
#         print("No data found. Please input data first.")
#         return
#     minimum, maximum, total, average = get_statistics(data)
#     print("\nDataset Statistics:")
#     print(f"Minimum value: {minimum}")
#     print(f"Maximum value: {maximum}")
#     print(f"Sum of all values: {total}")
#     print(f"Average value: {average}")


# data = []


# while True:
#     display_menu()
#     choice = input("\nPlease enter your choice: ")

#     if choice == '1':
#         input_data()
#     elif choice == '2':
#         data_summary()
#     elif choice == '3':
#         calculate_factorial()
#     elif choice == '4':
#         filter_data_by_threshold()
#     elif choice == '5':
#         sort_data()
#     elif choice == '6':
#         display_statistics()
#     elif choice == '7':
#         print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please enter a number from 1 to 7.")


def rss(*args):
    r=input("Enter data for 1D array (seperated by spaces): ")
    rr=r.split()
    for r in rr:
        slist.append(int(r))
    return args

def av():
    suum=sum(slist)
    leen=len(slist)
    avv=suum/leen
    return avv

def multiple():
    minv=min(slist)
    maxv=max(slist)
    suum=sum(slist)
    l=len(slist)
    aav=sum(slist)/l
    return {"minv":minv,"maxv":maxv,"suum":suum,"aav":aav}

def fac(n):
    if n<=1:
        return 1
    return n*fac(n-1)

slist=[]

while 1<2:
    print("""
Welcome to the Data Analyzer and Transformer Program

Main Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data by Threshold
5. Sort Data
6. Display Dataset Statistics
7. Exit Program
""")
    a=int(input("Enter your choice: "))
    if a==7:
        print("\nThank You for Using Data Analyzer and Transformer Program !")
        break
    elif a==1:
        rss()
        print("\nData has been stored successfully!")
    elif a==2:
        print("Data Summary:")
        print(f"- Total elements: {len(slist)}")
        print(f"- Minimum Value: {min(slist)}")
        print(f"- Maximum Value: {max(slist)}")
        print(f"- Sum of all Values: {sum(slist)}")
        result=av()
        print(f"- Average value: {result}")
    elif a==3:
        a=int(input("Enter number to find its factorial: "))
        print(f"\nFactorial of {a} is: {fac(a)}")
    elif a==4:
        b=int(input("Enter a threshold to filter out data above this value: "))
        sortlist=[]
        for s in slist:
            if s>=b:
                sortlist.append(s)
        print(f"Filtered Data (values >= {b})")
        print(sortlist)
    elif a==5:
        print("Choose sorting options:")
        print("1. Ascending")
        print("2. descending")
        p=int(input("Enter your choice: "))
        if p==1:
            slist.sort()
            print("Sorted data in Ascending Order:")
            print(slist)
        elif p==2:
            slist.sort(reverse=True)
            print("Sorted data in Descending Order:")
            print(slist)
        else:
            print("Enter 1 or 2 only !!")
    elif a==6:
        print("Data Statictics:")
        mul=multiple()
        print(f"- Minimum Value: {mul["minv"]}")
        print(f"- Maximum Value: {mul["maxv"]}")
        print(f"- Sum of all Values: {mul["suum"]}")
        print(f"- Average of Values: {mul["aav"]}")