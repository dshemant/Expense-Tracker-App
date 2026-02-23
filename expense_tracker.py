import csv

def add_expense():
    try:
        Item = input("Enter the items (e.g.Apple,Mobie): ")
        Price = float(input("Enter the price of the item : "))
        with open("expense.csv" , "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([Item,Price])
            print("Expense Saved!")
    except ValueError:
        print("Invalid Input, please enter valid values!!!!")

def view_expense():
    try:
        with open("expense.csv","r") as file:
            reader = csv.reader(file)
            print("\nItem  |  Price")
            print("________________")
            for row in reader:
                print(f"{row[0]}  |  {row[1]}")
    except FileNotFoundError:
        print("File not Found!!!!")


try:
    while True:
        choose = int(input("\n1.Add Expense\n2.View Expense\n3.Exit : "))
        if choose == 1:
            print("You choose add expense")
            add_expense()
        elif choose == 2:
            print("You choose view expense")
            view_expense()
        elif choose == 3:
            break
except ValueError:
    print("Invalid Input!!!!!")
