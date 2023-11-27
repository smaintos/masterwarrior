from __future__ import annotations
print("\n")

from dice import Dice



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
        super().__init__(name, max_hp=20, attack=8, defense=3, speed=0, dice=Dice(6))

    def compute_damages(self, roll, target: Character):
        print("🪓 Bonus: Axe in your face (+3 attack)")
        return super().compute_damages(roll, target) + 3 

class Mage(Character):
    def __init__(self, name: str):
        super().__init__(name, max_hp=20, attack=8, defense=3, speed=0, dice=Dice(6))

    def compute_defense(self, damages, roll, attacker: Character):
        print("🧙 Bonus: Magic armor (-3 damages)")
        return super().compute_defense(damages, roll, attacker) - 3

class Thief(Character):
    def __init__(self, name: str):
        super().__init__(name, max_hp=20, attack=8, defense=3, speed=0, dice=Dice(6))

    def compute_damages(self, roll, target: Character):
        print(f"🔪 Bonus: Sneaky attack (+{target.get_defense_value()} damages)")
        return super().compute_damages(roll, target) + target.get_defense_value()

class Knight(Character):
    def __init__(self, name: str):
        super().__init__(name, max_hp=20, attack=2, defense=2, speed=2, dice=Dice(6))

    def compute_damages(self, roll, target: Character):
        print("⚔️ Bonus: Charging attack (+2 attack)")
        return super().compute_damages(roll, target)

