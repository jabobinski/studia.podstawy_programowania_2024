class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.items[item_id] = {"item_name": item_name, "stock_count": stock_count, "price": price}
        print(f"Item {item_name} added with item ID {item_id}")

    def update_item(self, item_id, item_name=None, stock_count=None, price=None):
        if item_id in self.items:
            if item_name is not None:
                self.items[item_id]["item_name"] = item_name
            if stock_count is not None:
                self.items[item_id]["stock_count"] = stock_count
            if price is not None:
                self.items[item_id]["price"] = price
            print(f"Item {self.items[item_id]['item_name']} updated")
        else:
            print("Item not found")

    def check_item_details(self, item_id):
        if item_id in self.items:
            details = self.items[item_id]
            print(f"Item ID: {item_id}, Item Name: {details['item_name']}, Stock Count: {details['stock_count']}, Price: ${details['price']}")
        else:
            print("Item not found")

inventory = Inventory()

inventory.add_item("001", "Laptop", 10, 1000)
inventory.add_item("002", "Phone", 20, 500)

inventory.update_item("001", item_name="New Laptop", price=1200)

inventory.check_item_details("001")
inventory.check_item_details("003") 