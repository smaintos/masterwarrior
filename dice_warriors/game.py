from team import teamplayer, teamenemy
from utils import press_enter_to_continue
from character import Character, Warrior, Mage, Thief, Knight
from message_manager import MessageManager
import random


def display_enemy_info(enemy_team):
    print("\nÉquipe ennemie:")
    for i, character in enumerate(enemy_team, start=1):
        character.show_enemy_info()
        print(f"{i}. {character}")


def choose_target(target_team, is_player_turn):
    display_enemy_info(target_team)

    while True:
        target_index = int(input("Enter the number of your choice: ")) - 1

        if is_player_turn:
            if 0 <= target_index < len(target_team):
                target = target_team[target_index]
                if target.is_alive():
                    return target
                else:
                    print("You cannot choose a dead enemy. Please select another.")
            else:
                print("Invalid choice. Please enter a valid number.")
        else:
            print("It's not your turn to choose a target.")
            return None

    display_enemy_info(target_team)

    while True:
        target_index = int(input("Entrez le numéro de votre choix : ")) - 1

        if 0 <= target_index < len(target_team):
            target = target_team[target_index]
            if target.is_alive() and is_player_turn:
                return target
            elif not target.is_alive():
                print("Vous ne pouvez pas choisir un ennemi déjà vaincu. Veuillez en choisir un autre.")
            elif not is_player_turn:
                print("Ce n'est pas à votre tour de choisir la cible.")
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")


def choose_target_for_player(attacker, target_team):
    return choose_target(target_team, is_player_turn=True)


def choose_target_preference():
    choice = input("Voulez-vous choisir la cible de vos attaques ? (o/n) : ")
    return choice.lower() == 'o'


if __name__ == "__main__":
    print("Bienvenue dans Master Warrior !\n")
    player_team = teamplayer()
    enemy_team = teamenemy()

    print("\nVotre équipe :")
    for character in player_team:
        print(character)

    print("\nÉquipe ennemie :")
    for character in enemy_team:
        character.show_enemy_info()
        print(character)

    select_target_preference = choose_target_preference()
    is_player_turn = True  # Ajout de l'initialisation ici

    order_of_play = player_team + enemy_team
    order_of_play.sort(key=lambda x: x.get_speed(), reverse=True)

    print("\nOrdre d'attaque :")
    for i, character in enumerate(order_of_play, start=1):
        print(f"{i}. {character}")

    print("\nQue le combat commence !\n")

# ...

while any(character.is_alive() for character in order_of_play):
    for character in order_of_play:
        if not character.is_alive():
            print(f"{character.get_name()} is already defeated. Skipping their turn.")
            continue

        target_team = enemy_team if isinstance(character, Character) else player_team
        is_player_turn = isinstance(character, Character) and character in player_team

        print(f"\nCurrent character: {character}")

        if is_player_turn:
            if select_target_preference:
                print("\nChoose the target:")
                target = choose_target(target_team, is_player_turn)

                if target and not target.is_alive():
                    print(f"{target.get_name()} is already defeated. Choose another target.")
                    continue
            else:
                target = random.choice([c for c in target_team if c.is_alive()])

            character.attack(target)

            if not any(c.is_alive() for c in enemy_team):
                MessageManager.show_victory_message()
                break
        else:
            # Laissez les ennemis attaquer automatiquement, mais choisissez la cible aléatoirement
            alive_targets = [t for t in player_team if t.is_alive()]
            if alive_targets:
                target = random.choice(alive_targets)
                character.attack(target)

                if not any(c.is_alive() for c in player_team):
                    MessageManager.show_defeat_message()
                    break

    press_enter_to_continue()
