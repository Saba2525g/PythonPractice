print("SIMPLE CALCULATOR")
print("=" * 30)

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

print("\nresults:")
print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)

if num2 != 0:
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Cannot divide by zero")