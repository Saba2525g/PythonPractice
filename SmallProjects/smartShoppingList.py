import json
import os

class ShoppingList:
    def _init_(self):
        self.items = []
        self.file_name = "shopping_list.json"
        self.load_list()

    def load_list(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                 self.items = json.load(f)
        except FileNotFoundError:
            self.items = []

    def save_list(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(self.items, f, ensure_ascii=False, indent=2)

    def add_item(self):
        print("\n" + "=" * 40)
        print("ADD NEW ITEM")
        print("=" * 40)


        name = input("Item name: ")
        if not name:
            print("Item name cannot be empty!")
            return

        try:
            price = float(input("Item price: "))
            quantity = int(input("Item quantity: "))
        except ValueError:
            print("invalid price or quantity!")
            return

        item =
            "name": name,
            "price": price,
            "quantity": quantity,
            "total": price * quantity
        }

        self.items.append(item)
        self.save_list()
        print(f"\n'{name}' added to your shopping list.")