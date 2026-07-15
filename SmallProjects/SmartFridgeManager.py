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

    def show_expiring_soon(self):
        print("\n" + "=" * 50)
        print("FOODS EXPIRING SOON")
        print("=" * 50)

        soon = [f for f in self.foods if 0 <= f["days_left"] <= 3]
        expired = [f for f in self.foods if f["days_left"] < 0]

        if expired:
            print("\nEXPIRED FOODS:")
            for f in expired:
                print(f"   - {f['name']} ({f['quantity']}) - Expired {abs(f['days_left'])} days ago")

        if soon:
            print("\nEXPIRING SOON (3 days or less):")
            for f in soon:
                print(f"   - {f['name']} ({f['quantity']}) - {f['days_left']} days left")

        if not expired and not soon:
            print("\nNo food is expiring soon!")

        if expired or soon:
            print("\nSuggestion: Use these foods first!")

    def delete_food(self):
        if not self.foods:
            print("\nYour inventory is empty!")
            return

        self.show_inventory()
        try:
            choice = int(input("\nEnter food number to delete: "))
            if 1 <= choice <= len(self.foods):
                removed = self.foods.pop(choice - 1)
                self.save_data()
                print(f"\n'{removed['name']}' removed from inventory!")
            else:
                print("Invalid number!")
        except ValueError:
            print("Please enter a number!")

    def generate_shopping_list(self):
        print("\n" + "=" * 50)
        print("SHOPPING LIST GENERATOR")
        print("=" * 50)

        expired = [f for f in self.foods if f["days_left"] < 0]

        if expired:
            print("\nFoods to buy (expired):")
            for f in expired:
                print(f"   - {f['name']} (need {f['quantity']})")
        else:
            print("\nNo expired foods! You're doing great!")

        low_quantity = [f for f in self.foods if f["quantity"] <= 2 and f["days_left"] > 0]
        if low_quantity:
            print("\nFoods running low:")
            for f in low_quantity:
                print(f"   - {f['name']} (only {f['quantity']} left)")

    def meal_suggestion(self):
        print("\n" + "=" * 50)
        print("MEAL SUGGESTION")
        print("=" * 50)

        soon_foods = [f for f in self.foods if 0 <= f["days_left"] <= 3]

        if soon_foods:
            print("\nMake a meal with these foods that expire soon:")
            meal = [f["name"] for f in soon_foods[:3]]
            print(f"   Try: {', '.join(meal)}")
            print("   Tip: Use them today or tomorrow!")
        else:
            print("\nYour food is fresh. Plan meals for the week")

    def get_stats(self):
        if not self.foods:
            print("\nNo foods in inventory!")
            return

        total_items = len(self.foods)
        total_quantity = sum(f["quantity"] for f in self.foods)
        expired = len([f for f in self.foods if f["days_left"] < 0])

        print("\n" + "=" * 50)
        print("INVENTORY STATS")
        print("=" * 50)
        print(f"Total food types: {total_items}")
        print(f"Total items: {total_quantity}")

        if expired == 0:
            print("Expired items: None! Great job!")
        else:
            print(f"Expired items: {expired}")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_menu(self):
        print("\n" + "=" * 50)
        print("FOOD WASTE MANAGER")
        print("=" * 50)
        print("1. Add Food")
        print("2. View Inventory")
        print("3. Show Expiring Soon")
        print("4. Delete Food")
        print("5. Generate Shopping List")
        print("6. Get Meal Suggestion")
        print("7. View Stats")
        print("8. Exit")
        print("=" * 50)

    def run(self):
        while True:
            self.clear_screen()
            self.show_menu()

            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                self.clear_screen()
                self.add_food()
                input("\nPress Enter to continue...")

            elif choice == "2":
                self.clear_screen()
                self.show_inventory()
                input("\nPress Enter to continue...")

            elif choice == "3":
                self.clear_screen()
                self.show_expiring_soon()
                input("\nPress Enter to continue...")

            elif choice == "4":
                self.clear_screen()
                self.delete_food()
                input("\nPress Enter to continue...")

            elif choice == "5":
                self.clear_screen()
                self.generate_shopping_list()
                input("\nPress Enter to continue...")

            elif choice == "6":
                self.clear_screen()
                self.meal_suggestion()
                input("\nPress Enter to continue...")

            elif choice == "7":
                self.clear_screen()
                self.get_stats()
                input("\nPress Enter to continue...")

            elif choice == "8":
                print("\nGoodbye! Reduce waste, save the planet!")
                break

            else:
                print("\nInvalid choice!")
                input("\nPress Enter to continue...")


if __name__ == "__main__":
    app = FoodWasteManager()
    app.run()