import json
import os
from datetime import datetime


class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.file_name = "employees.json"
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                self.employees = json.load(f)
        except FileNotFoundError:
            self.employees = []

    def save_data(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(self.employees, f, ensure_ascii=False, indent=2)

    def add_employee(self):
        print("\n" + "=" * 50)
        print("ADD NEW EMPLOYEE")
        print("=" * 50)

        name = input("full name: ")
        position = input("position: ")
        salary = float(input("Salary: "))
        department = input("department: ")

        employee = {
            "id": len(self.employees) + 1,
            "name": name,
            "position": position,
            "salary": salary,
            "department": department,
            "hire_date": datetime.now().strftime("%Y-%m-%d"),
            "active": True
        }

        self.employees.append(employee)
        self.save_data()
        print(f"\nEmployee '{name}' added successfully!")

    def show_all_employees(self):
        if not self.employees:
            print("\nNo employees found!")
            return

        print("\n" + "=" * 60)
        print("ALL EMPLOYEES")
        print("=" * 60)

        for emp in self.employees:
            status = "Active" if emp["active"] else "Inactive"
            print(f"ID: {emp['id']}")
            print(f"Name: {emp['name']}")
            print(f"Position: {emp['position']}")
            print(f"Salary: ${emp['salary']:,.2f}")
            print(f"Department: {emp['department']}")
            print(f"Status: {status}")
            print("-" * 50)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_menu(self):
        print("\n" + "=" * 50)
        print("EMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Employee")
        print("2. Show All Employees")
        print("3. Exit")
        print("=" * 50)

    def run(self):
        while True:
            self.clear_screen()
            self.show_menu()

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.clear_screen()
                self.add_employee()
                input("\nPress Enter to continue...")
            elif choice == "2":
                self.clear_screen()
                self.show_all_employees()
                input("\nPress Enter to continue...")
            elif choice == "3":
                print("\nGoodbye!")
                break
            else:
                print("\ninvalid choice!")
                input("\nPress Enter to continue...")


if __name__ == "__main__":
    app = EmployeeManager()
    app.run()