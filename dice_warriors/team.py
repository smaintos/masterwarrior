from character import Warrior, Mage, Thief, Knight

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
            team_player.append(Warrior(name))
        elif choice == "2":
            team_player.append(Mage(name))
        elif choice == "3":
            team_player.append(Thief(name))
        elif choice == "4":
            team_player.append(Knight(name))
        else:
            print("Invalid choice. Defaulting to Warrior.")
            team_player.append(Warrior(name))
            
    for character in team_player:
        character._speed = character._dice.roll()
    team_player.sort(key=lambda x: x.get_speed(), reverse=True)
    
    return team_player

def teamenemy():
    team_enemy = []
    for i in range(4):
        name = f"Enemy {i+1}"
        print(f"\nChoose the class for {name}:")
        print("1. Warrior (Tanky, +3 attack)")
        print("2. Mage (Defensive, +3 defense)")
        print("3. Thief (Agile, ignores defense)")
        print("4. Knight (Balanced, +2 speed)")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            team_enemy.append(Warrior(name))
        elif choice == "2":
            team_enemy.append(Mage(name))
        elif choice == "3":
            team_enemy.append(Thief(name))
        elif choice == "4":
            team_enemy.append(Knight(name))
        else:
            print("Invalid choice. Defaulting to Warrior.")
            team_enemy.append(Warrior(name))

    for character in team_enemy:
        character._speed = character._dice.roll()
    team_enemy.sort(key=lambda x: x.get_speed(), reverse=True)

    return team_enemy