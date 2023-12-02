from __future__ import annotations
from team import teamplayer, teamenemy
from utils import press_enter_to_continue
from character import Character, Warrior, Mage, Thief, Knight
from message_manager import MessageManager  # Import the MessageManager class
import random

def display_enemy_info(enemy_team):
    print("\nEnemy team:")
    for i, character in enumerate(enemy_team, start=1):
        character.show_enemy_info()
        print(f"{i}. {character}")

def choose_target(target_team):
    display_enemy_info(target_team)
    
    while True:
        target_index = int(input("Enter the number of your choice: ")) - 1

        if 0 <= target_index < len(target_team):
            target = target_team[target_index]
            if target.is_alive():
                return target
            else:
                print("You cannot choose a dead enemy. Please select another.")
        else:
            print("Invalid choice. Please enter a valid number.")

def choose_target_preference():
    choice = input("Do you want to choose the target of your attacks? (y/n): ")
    return choice.lower() == 'y'

if __name__ == "__main__":
    print("Welcome to Master Warrior ! \n")
    player_team = teamplayer()
    enemy_team = teamenemy()

    print("\nYour team:")
    for character in player_team:
        print(character)

    # Ajout de l'étape pour choisir la préférence du joueur avant le combat
    select_target_preference = choose_target_preference()

    order_of_play = player_team + enemy_team
    order_of_play.sort(key=lambda x: x.get_speed(), reverse=True)

    print("\nLet the battle begin!\n")

    while any(character.is_alive() for character in player_team):
        for character in player_team:
            target_team = enemy_team

            print(f"\nCurrent character: {character}")
        
        # Utilisation de la variable select_target_preference pour déterminer si le joueur choisit la cible
        if select_target_preference:
            print("\nChoose the target:")
            target = choose_target(target_team)
            
            # Vérifiez si la cible est vivante avant d'attaquer
            if not target.is_alive():
                print(f"{target.get_name()} is already defeated. Choose another target.")
                continue
        else:
            target = random.choice([c for c in target_team if c.is_alive()])

        character.attack(target)

        if not any(character.is_alive() for character in enemy_team):
            MessageManager.show_victory_message()
            break

    # Laissez les ennemis attaquer automatiquement après que le joueur ait terminé ses attaques
        for enemy in enemy_team:
            target_team = player_team
            alive_targets = [t for t in target_team if t.is_alive()]

            if alive_targets:
                target = random.choice(alive_targets)
                enemy.attack(target)

        if not any(character.is_alive() for character in player_team):
            MessageManager.show_defeat_message()
            break



    press_enter_to_continue()
