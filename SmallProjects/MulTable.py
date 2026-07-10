print("MULTIPLICATION TABLE")
print("=" * 20)

number = int(input("Enter a number: "))

print("\nMULTIPLICATION TABLE OF" ,number)
print("=" * 20)

for i in range(1,11):
    print(number,"*",i,"=",i*number)