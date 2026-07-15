import json
import os
from datetime import datetime


class FoodWasteManager:
    def __init__(self):
        self.foods = []
        self.file_name = "food_inventory.json"
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                self.foods = json.load(f)
        except FileNotFoundError:
            self.foods = []

    def save_data(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(self.foods, f, ensure_ascii=False, indent=2)

    def add_food(self):
        print("\n" + "=" * 50)
        print("ADD FOOD ITEM")
        print("=" * 50)

        name = input("food name: ")
        if not name:
            print("name cannot be empty!")
            return

        try:
            quantity = int(input("Quantity: "))
            expiry = input("expiry date (YYYY-MM-DD): ")

            expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
            days_left = (expiry_date - datetime.now()).days

            food = {
                "name": name,
                "quantity": quantity,
                "expiry": expiry,
                "days_left": days_left
            }

            self.foods.append(food)
            self.save_data()
            print(f"\n'{name}' added to your inventory!")

            if days_left <= 3 and days_left >= 0:
                print(f"Warning: '{name}' expires in {days_left} days!")
            elif days_left < 0:
                print(f"'{name}' is already expired!")

        except ValueError:
            print("invalid input! Please check the format.")

    def show_inventory(self):
        if not self.foods:
            print("\nYour inventory is empty!")
            return

        print("\n" + "=" * 60)
        print("YOUR FOOD INVENTORY")
        print("=" * 60)

        sorted_foods = sorted(self.foods, key=lambda x: x["days_left"])

        for i, food in enumerate(sorted_foods, 1):
            days = food["days_left"]
            status = "Fresh"
            if days < 0:
                status = "EXPIRED!"
            elif days <= 2:
                status = "URGENT!"
            elif days <= 5:
                status = "Soon"

            print(f"{i}. {food['name']}")
            print(f"   Quantity: {food['quantity']}")
            print(f"   Expiry: {food['expiry']} ({days} days left)")
            print(f"   Status: {status}")
            print("-" * 50)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_menu(self):
        print("\n" + "=" * 50)
        print("FOOD WASTE MANAGER")
        print("=" * 50)
        print("1. Add Food")
        print("2. View Inventory")
        print("3. Exit")
        print("=" * 50)

    def run(self):
        while True:
            self.clear_screen()
            self.show_menu()

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.clear_screen()
                self.add_food()
                input("\nPress Enter to continue...")

            elif choice == "2":
                self.clear_screen()
                self.show_inventory()
                input("\nPress Enter to continue...")

            elif choice == "3":
                print("\nGoodbye! Reduce waste, save the planet!")
                break

            else:
                print("\nInvalid choice!")
                input("\nPress Enter to continue...")


if __name__ == "__main__":
    app = FoodWasteManager()
    app.run()