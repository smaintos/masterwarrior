import logging

logging.basicConfig(filename='game_log.log', level=logging.INFO)

def log_battle_summary(player_team, enemy_team):
    for character in player_team:
        logging.info(f"Player Team - {character.get_name()}: HP = {character._current_hp}, Attack = {character._attack_value}, Defense = {character._defense_value}, Speed = {character._speed}")

    for character in enemy_team:
        logging.info(f"Enemy Team - {character.get_name()}: HP = {character._current_hp}, Attack = {character._attack_value}, Defense = {character._defense_value}, Speed = {character._speed}")

def log_attack_summary(attacker, target, damages):
    logging.info(f"{attacker.get_name()} attacked {target.get_name()} with {damages} damages")

def log_defense_summary(defender, attacker, wounds):
    logging.info(f"{defender.get_name()} defended against {attacker.get_name()} and took {wounds} wounds")

def log_round_separator():
    logging.info("=" * 30)

if __name__ == "__main__":
    from team import teamplayer, teamenemy
    from utils import press_enter_to_continue
    from character import Character
    import random

    print("Welcome to Master Warrior!\n")
    player_team = teamplayer()
    enemy_team = teamenemy()

    log_battle_summary(player_team, enemy_team)

    order_of_play = player_team + enemy_team
    order_of_play.sort(key=lambda x: x.get_speed(), reverse=True)

    print("\nLet the battle begin!\n")

    while any(character.is_alive() for character in order_of_play):
        for character in order_of_play:
            target_team = enemy_team if isinstance(character, Character) and character in player_team else player_team
            target = random.choice([c for c in target_team if c.is_alive()])
            damages = character.attack(target)
            log_attack_summary(character, target, damages)
            if target.is_alive():
                target.defense(damages, character)
                log_defense_summary(target, character, damages)

        if any(character.is_alive() for character in player_team + enemy_team):
            log_round_separator()
            press_enter_to_continue()

    log_battle_summary(player_team, enemy_team)
    logging.shutdown()
