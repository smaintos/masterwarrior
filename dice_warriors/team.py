from character import Warrior, Mage, Thief, Knight
import random

def teamplayer():
    team_player = []
    for i in range(4):
        name = input(f"Enter the name for character {i+1}: ")
        print("\nChoose the class for character:")
        print("1. Warrior (Tanky, +3 attack)")
        print("2. Mage (Defensive, +3 defense)")
        print("3. Thief (Agile, ignores defense)")
        print("4. Knight (Balanced, +2 speed)")
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            character = Warrior(name)
        elif choice == "2":
            character = Mage(name)
        elif choice == "3":
            character = Thief(name)
        elif choice == "4":
            character = Knight(name)
        else:
            print("Invalid choice. Defaulting to Warrior.")
            character = Warrior(name)

        character.regenerate()  # Régénère les HP
        team_player.append(character)
            
    for character in team_player:
        character._speed = character._dice.roll()
    team_player.sort(key=lambda x: x.get_speed(), reverse=True)
    
    return team_player

def teamenemy():
    team_enemy = []
    for i in range(4):
        name = f"Enemy {i + 1}"
        
        # Ajoutez cette vérification pour permettre au joueur de choisir la classe de l'adversaire
        choice = input(f"Do you want to choose the class for {name}? (y/n): ")
        if choice.lower() == 'y':
            print("\nChoose the class for character:")
            print("1. Warrior (Tanky, +3 attack)")
            print("2. Mage (Defensive, +3 defense)")
            print("3. Thief (Agile, ignores defense)")
            print("4. Knight (Balanced, +2 speed)")
            class_choice = input("Enter the number of your choice: ")

            if class_choice == "1":
                team_enemy.append(Warrior(name))
            elif class_choice == "2":
                team_enemy.append(Mage(name))
            elif class_choice == "3":
                team_enemy.append(Thief(name))
            elif class_choice == "4":
                team_enemy.append(Knight(name))
            else:
                print("Invalid choice. Defaulting to Warrior.")
                team_enemy.append(Warrior(name))
        else:
            team_enemy.append(random.choice([Warrior(name), Mage(name), Thief(name), Knight(name)]))

    for character in team_enemy:
        character._speed = character._dice.roll()
    team_enemy.sort(key=lambda x: x.get_speed(), reverse=True)

    return team_enemy
