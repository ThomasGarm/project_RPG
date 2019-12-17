"""game's mechanics"""
from characters.guerrier import Guerrier
from characters.archer import Archer
from characters.thomas_le_méchant import Thomas_le_méchant
from characters.magicien import Magicien
class Game:
    def __init__(self):
        self.nom = None
        self.perso = None
        self.ennemy = None
        #super().__init__(vie, attaque, défense, agilité)
        
    """def player_name(self):
        self.nom= input("Quel est votre nom ?")
        print(f"Bienvenue {self.nom}, jeune padawan de la programmation !")

    def character_choice(self):
        self.perso = input("gg").lower()
        if self.perso == "guerrier":
            return Guerrier()
        if self.perso == "archer":
            return Archer()
        if self.perso == "magicien":
            return Magicien()
        else:
            print("wrong")
            self.character_choice()"""
    def test_chara(self):
        self.perso = Guerrier()
            
    def test_ennemy(self):
        self.ennemy = Thomas_le_méchant()

    def __repr__(self):
        print (self.perso.vie)
        print(self.perso.attaque)

    """def ennemy_vs_player(self):
        player = input("  ")
        while self.perso.vie != 0 and self.ennemy.vie != 0:
            if player == "a":
                print(True)"""
    

        

