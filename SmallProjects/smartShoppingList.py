import json
import os


class ShoppingList:
    def __init__(self):
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
            print("item name cannot be empty!")
            return

        try:
            price = float(input("Price (in dollars): "))
            quantity = int(input("Quantity: "))
        except ValueError:
            print("Invalid price or quantity!")
            return

        item = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "total": price * quantity
        }

        self.items.append(item)
        self.save_list()
        print(f"\n'{name}' added to your shopping list!")

    def show_list(self):
        if not self.items:
            print("\nyour shopping list is empty!")
            return

        print("\n" + "=" * 50)
        print("YOUR SHOPPING LIST")
        print("=" * 50)

        total = 0
        for i, item in enumerate(self.items, 1):
            total = total + item["total"]
            print(f"{i}. {item['name']}")
            print(f"   Price: ${item['price']} x {item['quantity']} = ${item['total']}")
            print("-" * 40)

        print(f"\nTOTAL COST: ${total}")

        if self.items:
            cheapest = min(self.items, key=lambda x: x["price"])
            expensive = max(self.items, key=lambda x: x["price"])
            print(f"\nCheapest item: {cheapest['name']} (${cheapest['price']})")
            print(f"Most expensive: {expensive['name']} (${expensive['price']})")

    def delete_item(self):
        if not self.items:
            print("\nYour shopping list is empty!")
            return

        self.show_list()
        try:
            choice = int(input("\nenter item number to delete: "))
            if 1 <= choice <= len(self.items):
                removed = self.items.pop(choice - 1)
                self.save_list()
                print(f"\n'{removed['name']}' removed from your list!")
            else:
                print("Invalid number!")
        except ValueError:
            print("Please enter a number!")

    def edit_item(self):
        if not self.items:
            print("\nyour shopping list is empty!")
            return

        self.show_list()
        try:
            choice = int(input("\nEnter item number to edit: "))
            if 1 <= choice <= len(self.items):
                item = self.items[choice - 1]
                print(f"\nEditing: {item['name']}")

                new_name = input(f"New name (current: {item['name']}): ")
                if new_name:
                    item['name'] = new_name

                new_price = input(f"New price (current: ${item['price']}): ")
                if new_price:
                    item['price'] = float(new_price)

                new_qty = input(f"New quantity (current: {item['quantity']}): ")
                if new_qty:
                    item['quantity'] = int(new_qty)

                item['total'] = item['price'] * item['quantity']
                self.save_list()
                print("\nItem updated successfully!")
            else:
                print("invalid number!")
        except ValueError:
            print("Please enter a valid number!")

    def budget_check(self):
        if not self.items:
            print("\nYour shopping list is empty!")
            return

        total = sum(item["total"] for item in self.items)
        print("\n" + "=" * 40)
        print("BUDGET CHECKER")
        print("=" * 40)

        try:
            budget = float(input("Enter your budget: $"))
        except ValueError:
            print("Invalid budget!")
            return

        if total <= budget:
            print(f"\nYou're within budget! (${total} <= ${budget})")
            print(f"Remaining: ${budget - total}")
        else:
            print(f"\nYou're over budget! (${total} > ${budget})")
            print(f"Over by: ${total - budget}")

            sorted_items = sorted(self.items, key=lambda x: x["total"], reverse=True)
            print("\nSuggestions to reduce cost:")
            for item in sorted_items[:3]:
                print(f"   - Remove {item['name']} (save ${item['total']})")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_menu(self):
        print("\n" + "=" * 40)
        print("SMART SHOPPING LIST")
        print("=" * 40)
        print("1. Add item")
        print("2. View list")
        print("3. Delete item")
        print("4. Edit item")
        print("5. Check budget")
        print("6. Exit")
        print("=" * 40)

    def run(self):
        while True:
            self.clear_screen()
            self.show_menu()

            choice = input("enter your choice (1-6): ")

            if choice == "1":
                self.clear_screen()
                self.add_item()
                input("\nPress Enter to continue...")

            elif choice == "2":
                self.clear_screen()
                self.show_list()
                input("\nPress Enter to continue...")

            elif choice == "3":
                self.clear_screen()
                self.delete_item()
                input("\nPress Enter to continue...")

            elif choice == "4":
                self.clear_screen()
                self.edit_item()
                input("\nPress Enter to continue...")

            elif choice == "5":
                self.clear_screen()
                self.budget_check()
                input("\nPress Enter to continue...")

            elif choice == "6":
                print("\nGoodbye! Happy shopping!")
                break

            else:
                print("\nInvalid choice!")
                input("\nPress Enter to continue...")


if __name__ == "__main__":
    app = ShoppingList()
    app.run()