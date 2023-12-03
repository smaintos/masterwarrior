from rich.console import Console
from rich.theme import Theme

# Définir un thème avec des couleurs spécifiques
custom_theme = Theme({
    "victory": "bold green",
    "defeat": "bold red",
})

console = Console(theme=custom_theme)

class MessageManager:
    
    @staticmethod
    def show_victory_message():
        console.print("[victory]🎉 Félicitations ! Tu a gagné la game ![/victory]",justify="center")

    @staticmethod
    def show_defeat_message():
        console.print("[defeat]😔 Game over ! Tu a perdu la game L.[/defeat]",justify="center")
