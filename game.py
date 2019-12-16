"""game's mechanics"""

class Game:
    def __init__(self):
        self.nom = None
        
    def player_name(self):
        self.nom= input("Quel est votre nom ?")
        print(f"Bienvenue {self.nom} jeune padawan de la programmation")