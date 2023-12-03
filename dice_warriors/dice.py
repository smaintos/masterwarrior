from rich import print
import random

print("[center]\n[/center]")

class Dice:
    def __init__(self, faces=6):
        self._faces = faces

    def __str__(self):
        return f"J'ai {self._faces} faces."

    def roll(self):
        return random.randint(1, self._faces)


class RiggedDice(Dice):
    
    def roll(self, rigged=False):
        return self._faces if rigged else super().roll()
    
if __name__ == "__main__":
    a_dice = Dice()
    print(f"[cyan]{a_dice}[/cyan]")

    for _ in range(10):
        print(f"[green]{a_dice.roll()}[/green]")
