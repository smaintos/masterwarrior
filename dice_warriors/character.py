from __future__ import annotations
print("\n")

from dice import Dice

import random

class MessageManager():
    pass

class Character:
    
    def __init__(self, name: str, max_hp: int, attack: int, defense: int, speed: int, dice: Dice):
        self._name = name
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._attack_value = attack
        self._defense_value = defense
        self._speed = speed
        self._dice = dice

    def __str__(self):
        return f"""{self._name} the Character enters the arena with:
    ■ attack: {self._attack_value} 
    ■ defense: {self._defense_value}
    ■ speed: {self._speed}"""

    def get_defense_value(self):
        return self._defense_value
        
    def get_name(self):
        return self._name

    def get_speed(self):
        return self._speed
        
    def is_alive(self):
        return self._current_hp > 0       

    def show_healthbar(self):
        missing_hp = self._max_hp - self._current_hp
        healthbar = f"[{'♥' * self._current_hp}{'♡' * missing_hp}] {self._current_hp}/{self._max_hp}hp"
        print(healthbar)

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
        roll = self._dice.roll()
        damages = self.compute_damages(roll, target)
        print(f"⚔️ {self._name} attacks {target.get_name()} with {damages} damages (attack: {self._attack_value} + roll: {roll})")
        target.defense(damages, roll, self)
    
    def compute_defense(self, damages, roll, attacker):
        return damages - self._defense_value - roll
    
    def defense(self, damages, roll, attacker: Character):
        wounds = self.compute_defense(damages, roll, attacker)
        print(f"🛡️ {self._name} takes {wounds} wounds from {attacker.get_name()} (damages: {damages} - defense: {self._defense_value} - roll: {roll})")
        self.decrease_health(wounds)

class Warrior(Character):
    def __init__(self, name: str):
        super().__init__(name, max_hp=20, attack=8, defense=3, speed=1, dice=Dice(6))

    def compute_damages(self, roll, target: Character):
        print("🪓 Bonus: Axe in your face (+3 attack)")
        return super().compute_damages(roll, target) + 3 

class Mage(Character):
    def __init__(self, name: str):
        super().__init__(name, max_hp=20, attack=8, defense=3, speed=1, dice=Dice(6))

    def compute_defense(self, damages, roll, attacker: Character):
        print("🧙 Bonus: Magic armor (-3 damages)")
        return super().compute_defense(damages, roll, attacker) - 3

class Thief(Character):
    def __init__(self, name: str):
        super().__init__(name, max_hp=20, attack=8, defense=3, speed=1, dice=Dice(6))

    def compute_damages(self, roll, target: Character):
        print(f"🔪 Bonus: Sneaky attack (+{target.get_defense_value()} damages)")
        return super().compute_damages(roll, target) + target.get_defense_value()

class Knight(Character):
    def __init__(self, name: str):
        super().__init__(name, max_hp=20, attack=2, defense=2, speed=2, dice=Dice(6))

    def compute_damages(self, roll, target: Character):
        print("⚔️ Bonus: Charging attack (+2 attack)")
        return super().compute_damages(roll, target)

def create_team_player():
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
    return team_player

def create_team_enemy():
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

    # Roll for speed and sort characters by speed
    for character in team_enemy:
        character._speed = character._dice.roll()
    team_enemy.sort(key=lambda x: x.get_speed(), reverse=True)

    return team_enemy

def press_space_to_continue():
    input("Press [SPACE] to continue...")

if __name__ == "__main__":
    print("Welcome to the Arena!")
    player_team = create_team_player()
    enemy_team = create_team_enemy()

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
            press_space_to_continue()
