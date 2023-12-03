from rich import print
from rich.console import Console
from rich.theme import Theme
from team import teamplayer, teamenemy
from utils import press_enter_to_continue
from character import Character, Warrior, Mage, Thief, Knight
from message_manager import MessageManager
import random

# Définir un thème avec des couleurs spécifiques
custom_theme = Theme({
    "info": "cyan",
    "success": "green",
    "warning": "yellow",
    "error": "bold red",
})

console = Console(theme=custom_theme)

def display_enemy_info(enemy_team):
    console.print("\n[bold white]Équipe ennemie:[/bold white]")
    for i, character in enumerate(enemy_team, start=1):
        character.show_enemy_info()
        console.print(f"{i}. {character}") 

def choose_target_generic(target_team, is_player_turn):
    display_enemy_info(target_team)

    while True:
        target_index = int(input("Entrez le numéro de votre choix : " )) - 1

        if is_player_turn:
            if 0 <= target_index < len(target_team):
                target = target_team[target_index]
                if target.is_alive():
                    return target
                else:
                    console.print("[error]Vous ne pouvez pas choisir un ennemi déjà vaincu. Veuillez en choisir un autre.[/error]")
            else:
                console.print("[error]Choix invalide. Veuillez entrer un numéro valide.[/error]")
        else:
            console.print("[warning]Ce n'est pas à votre tour de choisir la cible.[/warning]")
            return None

def choose_target_for_player(attacker, target_team):
    return choose_target_generic(target_team, is_player_turn=True)

def choose_target_preference():
    choice = input("Voulez-vous choisir la cible de vos attaques ? (o/n) : ")
    return choice.lower() == 'o'

if __name__ == "__main__":
    console.print("Bienvenue dans Master Warrior !\n", style="bold magenta" , justify="center")

    player_team = teamplayer()
    enemy_team = teamenemy()

    console.print("\n[bold green]Votre équipe :[/bold green]")
    for character in player_team:
        console.print(f"{character}")

    console.print("\n[bold white]Équipe ennemie :[/bold white]")
    for character in enemy_team:
        character.show_enemy_info()
        console.print(f"{character}")

    select_target_preference = choose_target_preference()
    is_player_turn = True

    order_of_play = player_team + enemy_team
    order_of_play.sort(key=lambda x: x.get_speed(), reverse=True)

    console.print("\n[bold cyan]Ordre d'attaque :[/bold cyan]")
    for i, character in enumerate(order_of_play, start=1):
        console.print(f"{i}. {character}")

    console.print("\n[bold blue]Que le combat commence ![/bold blue]")

while any(character.is_alive() for character in order_of_play):
    for character in order_of_play:
        if not character.is_alive():
            console.print(f"{character.get_name()} est déjà vaincu. Passage à son tour.")
            continue

        target_team = enemy_team if isinstance(character, Character) else player_team
        is_player_turn = isinstance(character, Character) and character in player_team

        console.print(f"\n[info]Personnage actuel : {character}[/info]")

        if is_player_turn:
            if select_target_preference:
                console.print("\n[bold]Choisissez la cible :[/bold]")
                target = choose_target_generic(target_team, is_player_turn)

                if target and not target.is_alive():
                    console.print(f"[error]{target.get_name()} est déjà vaincu. Choisissez une autre cible.[/error]")
                    continue
            else:
                target = random.choice([c for c in target_team if c.is_alive()])

            character.attack(target)

            if not any(c.is_alive() for c in enemy_team):
                MessageManager.show_victory_message()
                press_enter_to_continue()
                exit()
                break
        else:
            alive_targets = [t for t in player_team if t.is_alive()]
            if alive_targets:
                target = random.choice(alive_targets)
                character.attack(target)

                if not any(c.is_alive() for c in player_team):
                    MessageManager.show_defeat_message()
                    press_enter_to_continue()
                    exit()
                    break
    press_enter_to_continue()
