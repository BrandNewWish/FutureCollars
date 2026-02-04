commands = [
    "balance",
    "sale",
    "purchase",
    "account",
    "list",
    "warehouse",
    "review",
    "end"
]


balance = 1000
warehouse = {}
operations = []
id_autoincrement = 0

def show_commands():
    print("Available commands")
    for index, command in enumerate(commands):
        print(f"{index}. {command}")

while True:
    show_commands()
    choice = input("Enter a command (name or number): ")

    if choice == "end" or choice == "7":
        print("Program ending")
        break

    elif choice == "balance" or choice == "0":
        print(f"Your Balance is {balance}")
        amount = float(input("Enter amount to add/subtract"))
        balance += amount
        operations.append(("balance", amount))
        print(f"New Balance: {balance}")

    elif choice == "sale" or choice == "1":
        product = input("Product name")
        if product not in warehouse:
            print("Product not found in warehouse!")
            continue
        price = float(input("Sale price"))
        quantity = int(input("Quantity"))
        if warehouse[product]["quantity"] < quantity:
            print("Not enough quantity in warehouse!")
            continue

        income = price * quantity
        balance += income
        warehouse[product]["quantity"] -= quantity
        operations.append(("sale", product, price,  quantity))
        print(f"Sold {quantity} x {product}. Income: {income}. New balance: {balance}")

    elif choice == "purchase" or choice == "2":
        product = input("Product name")
        price = float(input("Price per unit: "))
        quantity = int(input("Quantity: "))
        if quantity <=0 or price < 0:
            print("Invalid input")

        cost = price * quantity
        if balance < cost:
            print("Insufficient funds")
            continue
        else:
            if product not in warehouse:
                warehouse[product] = {"price": price, "quantity": quantity}
            else:
                warehouse[product]["quantity"] += quantity
            balance -= cost
            operations.append(("purchase", product, price, quantity))
            print(f"Purchased {quantity} x {product} for {cost}. New balance: {balance}")

    elif choice == "account" or choice == "3":
        print(f"Your current balance is {balance}")

    elif choice == "list" or choice == "4":
        if warehouse:
            print("Warehouse inventory:")
            for product, info in warehouse.items():
                print(f"{product} - price: {info['price']}, quantity: {info['quantity']}")
        else:
            print("Warehouse is empty")

    elif choice == "warehouse" or choice == "5":
        product = input("Enter product name:")
        info = warehouse.get(product)
        if product in warehouse:
            print(f"{product} -> price: {info['price']}, quantity: {info['quantity']}")
        else:
            print("Product not found.")

    elif choice == "review" or choice == "6":
        if not operations:
            print("No operations recorded yet")
            continue
        start_input = input("From index (empty = 0): ")
        end_input = input("To index (empty = last): ")

        start = int(start_input) if start_input != "" else 0
        end = int(end_input) if end_input != "" else len(operations)

        if start < 0 or end > len(operations) or start > end:
            print("Index out of range!")
            continue

        for i, op in enumerate(operations[start:end], start=start):
            print(f"{i}: {op}")