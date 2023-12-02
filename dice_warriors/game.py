from __future__ import annotations

from team import teamplayer, teamenemy
from utils import press_enter_to_continue
from character import Character, Warrior, Mage, Thief, Knight
from message_manager import MessageManager
import random

if __name__ == "__main__":
    print("Welcome to Master Warrior ! \n")
    player_team = teamplayer()

    # Create a list of random enemy classes
    enemy_classes = [Warrior, Mage, Thief, Knight]
    enemy_team = [random.choice(enemy_classes)(f"Enemy {i+1}") for i in range(len(player_team))]

    print("\nYour team:")
    for character in player_team:
        print(character)

    print("\nEnemy team:")
    for character in enemy_team:
        print(character)

    order_of_play = player_team + enemy_team
    order_of_play.sort(key=lambda x: x.get_speed(), reverse=True)

    print("\nLet the battle begin!\n")

    while any(character.is_alive() for character in order_of_play):
        for character in order_of_play:
            target_team = enemy_team if isinstance(character, Character) and character in player_team else player_team

            if any(c.is_alive() for c in target_team):
                print(f"\nCurrent character: {character}")

                choice = input("Do you want to choose the class of the target? (y/n): ")
                if choice.lower() == 'y':
                    print("\nChoose the class for target:")
                    print("1. Warrior (Tanky, +3 attack)")
                    print("2. Mage (Defensive, +3 defense)")
                    print("3. Thief (Agile, ignores defense)")
                    print("4. Knight (Balanced, +2 speed)")
                    class_choice = input("Enter the number of your choice: ")

                    if class_choice == "1":
                        target = next((c for c in target_team if isinstance(c, Warrior) and c.is_alive()), None)
                    elif class_choice == "2":
                        target = next((c for c in target_team if isinstance(c, Mage) and c.is_alive()), None)
                    elif class_choice == "3":
                        target = next((c for c in target_team if isinstance(c, Thief) and c.is_alive()), None)
                    elif class_choice == "4":
                        target = next((c for c in target_team if isinstance(c, Knight) and c.is_alive()), None)
                    else:
                        print("Invalid choice. Defaulting to a random target.")
                        target = random.choice([c for c in target_team if c.is_alive()])
                else:
                    target = random.choice([c for c in target_team if c.is_alive()])

                character.attack(target)

        if not any(character.is_alive() for character in player_team):
            MessageManager.show_defeat_message()
            break

        if not any(character.is_alive() for character in enemy_team):
            MessageManager.show_victory_message()
            break

        press_enter_to_continue()
