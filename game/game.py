"""game's mechanics"""
from characters.guerrier import Guerrier
from characters.archer import Archer
from characters.thomas_le_méchant import Thomas_le_méchant
from characters.magicien import Magicien
from game.naration import *
from characters.personnage import Personnage


class Game:
    
    
    def __init__(self):
        self.nom = None
        self.perso = None
        self.ennemy = None
        self.guerrier = Guerrier()
        
        
        
    def player_name(self):
        partie1()
        self.nom= input("Quel est votre nom ?")
        print(f"Bienvenue {self.nom}, jeune padawan de la programmation !")
    
    
    def character_choice(self):
        
        print("[GUERRIER] |[ARCHER] | [MAGICIEN]")
        self.perso = input("Choisissez un aventurier parmis ces trois personnage :").lower()
        if self.perso == "guerrier":
            self.perso = Guerrier()
            return self.perso
                
        if self.perso == "archer":
            self.perso = Archer()
            return self.perso
        if self.perso == "magicien":
            return Magicien()
        else:
            print("je connais pas cette aventurier !")
            self.character_choice()
    
    def test(self):
        print (f"Vous êtes un {self.perso}")
            
    def ennemy_choice(self,):
        self.ennemy = Thomas_le_méchant()
    
    
        
        


        
    def attack(self):
        attack = self.perso.attaque - self.ennemy.défense
        return self.ennemy.vie - attack

    #def esquive(self):
        
    def ennemy_vs_player(self):
        self.ennemy_choice()
        self.character_choice()
        print("Attaque: A , Fuir: F")
        player = input("Que choisissez-vous de faire ? ").lower()
        while self.perso.vie > 0 and self.ennemy.vie > 0:
            if player == "a":
               print (self.attack())
               
            # elif player == "f":
            #     print(True)
            # else:
            #     print("Choisissez entre A pour attaquer et F pour fuir")"""


