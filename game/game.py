"""game's mechanics"""
from characters.guerrier import Guerrier
from characters.archer import Archer
class Game:
    def __init__(self):
        self.nom = None
        self.perso = None
        
    def player_name(self):
        self.nom= input("Quel est votre nom ?")
        print(f"Bienvenue {self.nom}, jeune padawan de la programmation !")

    def character_choice(self):
        self.perso = input("gg").lower()
        if self.perso == "guerrier":
            return Guerrier()
        if self.perso == "archer"
            return Archer()
        

