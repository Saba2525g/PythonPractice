import math

print("CIRCLE CALCULATOR")
print("=" * 30)

radius = float(input("Enter radius: "))

area = math.pi * (radius ** 2)
circumference = 2 * math.pi * (radius)

print("\nresults:")
print("area: ", area)
print("circumference: ", circumference)