from datetime import datetime

print("AGE CALCULATOR")
print("=" * 30)

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month(1-12): "))
birth_day = int(input("Enter your birth day(1-31): "))

today = datetime.now()

age = today.year - birth_year

if (today.month, today.day) < (birth_month, birth_day):
          age = age - 1

print("your age is:", age , "years old")
