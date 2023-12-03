from __future__ import annotations
from rich.console import Console
from rich.theme import Theme
from datetime import datetime
from dice import Dice

# Définir un thème avec des couleurs spécifiques
custom_theme = Theme({
    "info": "cyan",
    "success": "green",
    "warning": "yellow",
    "error": "bold red",
})

console = Console(theme=custom_theme)

class MessageManager:
    def __init__(self, log_file="game_logs.txt"):
        self.log_file = log_file

    def log_message(self, message):
        with open(self.log_file, "a", encoding="utf-8") as file:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{current_time}] {message}\n")

class Character:
    message_manager = MessageManager()

    def __init__(self, name: str, max_hp: int, attack: int, defense: int, speed: int, dice: Dice):
        self._name = name
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._attack_value = attack
        self._defense_value = defense
        self._speed = speed
        self._dice = dice
        self.message_manager = Character.message_manager

    def __str__(self):
        return f"{self._name} le personnage entre dans l'arène avec:\n" \
               f"■ attaque : {self._attack_value}\n" \
               f"■ défense : {self._defense_value}\n" \
               f"■ vitesse : {self._speed}" if hasattr(self, '_name') else ""

    def get_defense_value(self):
        return self._defense_value

    def get_name(self):
        return self._name

    def get_speed(self):
        return self._speed

    def is_alive(self):
        return self._current_hp > 0

    def show_healthbar(self):
        missing_hp = max(0, self._max_hp - self._current_hp)
        healthbar = f"[{'♥' * self._current_hp}{'♡' * missing_hp}] {self._current_hp}/{self._max_hp}hp"
        message = f"{self._name}: {healthbar}"
        console.print(message, style="info", justify="center")
        self.message_manager.log_message(message)

    def show_enemy_info(self):
        healthbar = f"[{'♥' * self._current_hp}{'♡' * max(0, self._max_hp - self._current_hp)}] {self._current_hp}/{self._max_hp}hp"
        console.print(f"{self._name}: {healthbar}", style="info", justify="center")

    def regenerate(self):
        self._current_hp = self._max_hp

    def decrease_health(self, amount):
        self._current_hp -= amount
        if self._current_hp < 0:
            self._current_hp = 0
        self.show_healthbar()

    def compute_damages(self, roll, target):
        return self._attack_value + roll

    def attack(self, target: Character):
        if not self.is_alive():
            return
        attack_roll = self._dice.roll()
        defense_roll = target._dice.roll()

        damages = self.compute_damages(attack_roll, target)
        message = f"{self._name} attaque {target.get_name()} avec {damages} dégâts (attaque : {self._attack_value} + jet de dé: {attack_roll})"
        print(f"⚔️ {message}")
        self.message_manager.log_message(message)
        target.defense(damages, defense_roll, self)

    def compute_defense(self, damages, roll, attacker):
        return max(0, damages - self._defense_value - roll)

    def defense(self, damages, roll, attacker: Character):
        defense_roll = self._dice.roll()
        wounds = self.compute_defense(damages, defense_roll, attacker)
        print(f"🛡️ {self._name} subit {wounds} de blessures de {attacker.get_name()} (dégâts : {damages} - défense : {self._defense_value} - jet de dé : {defense_roll})")
        self.decrease_health(wounds)

class Warrior(Character):
    def __init__(self, name: str):
        super().__init__(name, max_hp=20, attack=8, defense=3, speed=0, dice=Dice(6))



class Mage(Character):
    def __init__(self, name: str):
        super().__init__(name, max_hp=20, attack=8, defense=3, speed=0, dice=Dice(6))



class Thief(Character):
    def __init__(self, name: str):
        super().__init__(name, max_hp=20, attack=8, defense=3, speed=0, dice=Dice(6))



class Knight(Character):
    def __init__(self, name: str):
        super().__init__(name, max_hp=20, attack=8, defense=3, speed=2, dice=Dice(6))

