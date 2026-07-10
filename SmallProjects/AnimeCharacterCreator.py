print("ANIME CHARACTER CREATOR")
print("=" * 30)
print("create your own anime character!")


name = input("Character name: ")
age = input("Age: ")
power = input("Special power: ")
color = input("Hair color: ")
weapon = input("Weapon: ")

character = {
    "name": name,
    "age": age,
    "power": power,
    "hair" : color,
    "weapon" : weapon
}

print("\n" + "=" * 35)
print("Your anime character")
print("=" * 35)
print("Name:", character["name"])
print("Age:", character["age"])
print("Power:", character["power"])
print("Hair Color:", character["hair"])
print("Weapon:", character["weapon"])
print("=" * 35)
print("READY FOR BATTLE!")


print(f"\n{name} with {color} hair uses {power} with {weapon}!")
