from __future__ import annotations

from team import teamplayer, teamenemy
from utils import press_enter_to_continue
from character import Character
import random

if __name__ == "__main__":
    print("Welcome to Master Warrior ! \n")
    player_team = teamplayer()
    enemy_team = teamenemy()

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
            target = random.choice([c for c in target_team if c.is_alive()])
            character.attack(target)

        if any(character.is_alive() for character in player_team + enemy_team):
            press_enter_to_continue()
