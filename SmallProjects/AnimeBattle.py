import random
import time

print("ANIME BATTLE")
print("=" * 35)

player_health = 100
enemy_health = 100

print("your opponent : Demon lord\n")

while player_health > 0 and enemy_health > 0:
    print(f"your HP: {player_health}")
    print(f"Enemy HP: {enemy_health}")
    print("\n1.Attack")
    print("2.Heal")
    print("3. Run away (coward)")

    choice = input("your move:")

    if choice == "1":
        damage = random.randint()