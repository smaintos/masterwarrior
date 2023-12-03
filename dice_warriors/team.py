from rich.console import Console
from rich.theme import Theme
from character import Warrior, Mage, Thief, Knight, Character
import random

# Définir un thème avec des couleurs spécifiques
custom_theme = Theme({
    "info": "cyan",
    "success": "green",
    "warning": "yellow",
    "error": "bold red",
})

console = Console(theme=custom_theme)

def center_text(text, width):
    padding = " " * ((width - len(text)) // 2)
    return f"{padding}{text}"

def teamplayer():
    team_player = []
    for i in range(4):
        name = input(f"Entrez le nom pour le personnage {i + 1} : ") 
        console.print(center_text("\nChoisissez la classe pour le personnage :", console.width), style="info")
        console.print(center_text("1. Guerrier (Costaud, +3 attaque)", console.width), style="info")
        console.print(center_text("2. Mage (Défensif, +3 défense)", console.width), style="info")
        console.print(center_text("3. Voleur (Agile, ignore la défense)", console.width), style="info")
        console.print(center_text("4. Chevalier (Équilibré, +2 vitesse)", console.width), style="info")
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
            console.print("Choix invalide. Par défaut, Guerrier.", style="error")
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
            console.print(center_text("\nChoisissez la classe pour le personnage :", console.width), style="info")
            console.print(center_text("1. Guerrier (Costaud, +3 attaque)", console.width), style="info")
            console.print(center_text("2. Mage (Défensif, +3 défense)", console.width), style="info")
            console.print(center_text("3. Voleur (Agile, ignore la défense)", console.width), style="info")
            console.print(center_text("4. Chevalier (Équilibré, +2 vitesse)", console.width), style="info")
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
                console.print("Choix invalide. Par défaut, Guerrier.", style="error")
                team_enemy.append(Warrior(name))
        else:
            team_enemy.append(random.choice([Warrior(name), Mage(name), Thief(name), Knight(name)]))

    # Ajustez le calcul de la vitesse pour chaque ennemi
    for character in team_enemy:
        character._speed += character._dice.roll()
    team_enemy.sort(key=lambda x: x.get_speed(), reverse=True)

    return team_enemy
