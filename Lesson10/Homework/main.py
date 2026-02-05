from Helper import load_data
from Lesson10.Homework.Manager import  Manager, register_actions


def main():
    my_company = load_data("data.json")
    manager = Manager(my_company)
    register_actions(manager)
    
    while True:
        print("\n---Menu___")
        print("1. Balance")
        print("2. Sale")
        print("3. Purchase")
        print("4. List warehouse")
        print("5. Review operations")
        print("6. Exit")
        
        choice = input("Choose option: ")

        if choice == "1":
            manager.execute("balance")

        elif choice == "2":
            product = input("Product name: ")
            price = float(input("Sale price "))
            quantity = int(input("Quantity: "))
            manager.execute("sale", product, price, quantity)

        elif choice == "3":
            product = input("Product name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            manager.execute("purchase", product, price, quantity)

        elif choice == "4":
            manager.execute("list")

        elif choice == "5":
            manager.execute("review")

        elif choice == "6":
            my_company.save_to_file("data.json")
            print("Data saved. Program ending.")
            break

        else:
            print("Wrong option")

if __name__ == "__main__":
    main()
