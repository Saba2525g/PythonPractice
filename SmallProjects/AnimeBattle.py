import random
import time

print("ANIME BATTLE")
print("=" * 35)

player_health = 100
enemy_health = 100

print("Your opponent: Demon Lord\n")

while player_health > 0 and enemy_health > 0:
    print(f"Your HP: {player_health}")
    print(f"Enemy HP: {enemy_health}")
    print("\n1. Attack")
    print("2. Heal")
    print("3. Run away (coward)")

    choice = input("Your move: ")

    if choice == "1":
        damage = random.randint(10, 30)
        enemy_health = enemy_health - damage
        print(f"\nYou attacked! Dealt {damage} damage!")

        if enemy_health > 0:
            enemy_damage = random.randint(5, 25)
            player_health = player_health - enemy_damage
            print(f"Enemy attacked! You lost {enemy_damage} HP!")

    elif choice == "2":
        heal = random.randint(10, 30)
        player_health = min(player_health + heal, 100)
        print(f"\nYou healed! +{heal} HP!")

    elif choice == "3":
        print("\nYou ran away like a true coward!")
        break

    else:
        print("\nInvalid move!")

    time.sleep(1)
    print("-" * 35)

if player_health <= 0:
    print("\nYou lost! The Demon Lord wins!")
elif enemy_health <= 0:
    print("\nYou won! Demon Lord defeated!")
else:
    print("\nYou ran away... maybe next time!")