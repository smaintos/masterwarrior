from character import Warrior, Mage, Thief, Knight, Character
import random

def teamplayer():
    team_player = []
    for i in range(4):
        name = input(f"Entrez le nom pour le personnage {i + 1} : ")
        print("\nChoisissez la classe pour le personnage :")
        print("1. Guerrier (Costaud, +3 attaque)")
        print("2. Mage (Défensif, +3 défense)")
        print("3. Voleur (Agile, ignore la défense)")
        print("4. Chevalier (Équilibré, +2 vitesse)")
        choice = input("Entrez le numéro de votre choix : ")

        # Utilisation de la classe correcte en fonction du choix
        if choice == "1":
            character = Warrior(name)
        elif choice == "2":
            character = Mage(name)
        elif choice == "3":
            character = Thief(name)
        elif choice == "4":
            character = Knight(name)
        else:
            print("Choix invalide. Par défaut, Guerrier.")
            character = Warrior(name)

        character.regenerate()  # Régénère les HP
        team_player.append(character)

    # Ajustez le calcul de la vitesse pour chaque personnage
    for character in team_player:
        character._speed += character._dice.roll()
    team_player.sort(key=lambda x: x.get_speed(), reverse=True)

    return team_player

def teamenemy():
    team_enemy = []
    for i in range(4):
        name = f"Ennemi {i + 1}"

        # Demandez au joueur s'il souhaite choisir la classe de l'ennemi
        choice = input(f"Voulez-vous choisir la classe pour {name} ? (o/n) : ")
        if choice.lower() == 'o':
            print("\nChoisissez la classe pour le personnage :")
            print("1. Guerrier (Costaud, +3 attaque)")
            print("2. Mage (Défensif, +3 défense)")
            print("3. Voleur (Agile, ignore la défense)")
            print("4. Chevalier (Équilibré, +2 vitesse)")
            class_choice = input("Entrez le numéro de votre choix : ")

            # Utilisation de la classe correcte en fonction du choix
            if class_choice == "1":
                team_enemy.append(Warrior(name))
            elif class_choice == "2":
                team_enemy.append(Mage(name))
            elif class_choice == "3":
                team_enemy.append(Thief(name))
            elif class_choice == "4":
                team_enemy.append(Knight(name))
            else:
                print("Choix invalide. Par défaut, Guerrier.")
                team_enemy.append(Warrior(name))
        else:
            team_enemy.append(random.choice([Warrior(name), Mage(name), Thief(name), Knight(name)]))

    # Ajustez le calcul de la vitesse pour chaque ennemi
    for character in team_enemy:
        character._speed += character._dice.roll()
    team_enemy.sort(key=lambda x: x.get_speed(), reverse=True)

    return team_enemy