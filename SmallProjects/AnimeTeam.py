import random

print("CHOOSE YOUR ANIME TEAM")
print("=" * 35)

characters = ["Chuuya", "Dazai" ,"Mori" , "Akutagawa" , "Yosano" , "Atsushi" , "Fyodor"]

print("available characters:")

for i, char in enumerate(characters, 1):
         print(f"{i}. {char}")

print("\nyour team will be selected randomly!")
team = random.sample(characters, 3)

print("\nyour anime team:")
print("=" * 35)
for char in team:
    print(f"{char}")

print("\nteam power level:OVER 9000!")


