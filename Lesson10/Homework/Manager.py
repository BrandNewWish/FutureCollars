
class Manager:
    def __init__(self, data):
        self.data = data
        self.actions = {}

    def assign(self, name):
        def decorator(func):
            self.actions[name] = func
            return func
        return decorator

    def execute(self, name, *args, **kwargs):
        if name not in self.actions:
            print("Action not available.")
            return
        return self.actions[name](self, *args, **kwargs)

def register_actions(manager):

    @manager.assign("balance")
    def balance(manager):
        print("Current balance:", manager.data.balance)

    @manager.assign("sale")
    def sale(manager, product, price, quantity):
        warehouse = manager.data.warehouse

        if product not in warehouse:
            print("Product not found.")
            return

        if warehouse[product]["quantity"] < quantity:
            print("Not enough quantity.")
            return

        income = price * quantity
        warehouse[product]["quantity"] -= quantity
        manager.data.balance += income
        manager.data.operations.append(("sale", product, price, quantity))
        print("Sale completed.")

    @manager.assign("purchase")
    def purchase(manager, product, price, quantity):
        cost = price * quantity

        if manager.data.balance < cost:
            print("Insufficient funds.")
            return

        if product not in manager.data.warehouse:
            manager.data.warehouse[product] = {"price": price, "quantity": quantity}
        else:
            manager.data.warehouse[product]["quantity"] += quantity

        manager.data.balance -= cost
        manager.data.operations.append(("purchase", product, price, quantity))
        print("Purchase completed.")

    @manager.assign("list")
    def list_warehouse(manager):
        if not manager.data.warehouse:
            print("Warehouse is empty.")
            return
        for product, info in manager.data.warehouse.items():
            print(f"{product}: price={info['price']}, quantity={info['quantity']}")

    @manager.assign("review")
    def review(manager):
        if not manager.data.operations:
            print("No operations recorded.")
            return
        for i, op in enumerate(manager.data.operations):
            print(f"{i}: {op}")



