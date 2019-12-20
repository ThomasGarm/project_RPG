"""game's mechanics"""
from characters.guerrier import Guerrier
from characters.archer import Archer
from characters.thomas_le_méchant import Thomas_le_méchant
from characters.magicien import Magicien
from game.naration import *

class Game:
    def __init__(self):
        self.nom = None
        self.perso = None
        self.ennemy = None
        self.attack = None
        
    def player_name(self):
        partie1()
        self.nom= input("Quel est votre nom ? ").upper()
        print(f"Bienvenue {self.nom}, jeune padawan de la programmation !\n")

    def character_choice(self):
        print("[GUERRIER] |[ARCHER] | [MAGICIEN]\n")
        self.perso = input("Choisissez un aventurier parmis ces trois personnage :\n").lower()
        if self.perso == "guerrier":
            return Guerrier()
        elif self.perso == "archer":
            return Archer()
        elif self.perso == "magicien":
            return Magicien()
        else:
            print("je connais pas cette aventurier !")
            self.character_choice()
            
    def ennemy_choice(self):
        self.ennemy = Thomas_le_méchant()
        print("Thommas le méchant s'approche de vous armé de sa grande régles épineuse !\n")
        return self.ennemy

    def ennemy_vs_player(self, perso, ennemy):
        self.character_choice()
        self.ennemy_choice()
        while perso.vie > 0 and ennemy.vie > 0:
            print("[Attaque: A , Fuir: F]")
            action = input("Que choisissez-vous faire ? ").lower()
            if action == "a":
                self.fight_action(perso, ennemy)
                print(f"{self.perso} attaque violamment {self.ennemy.name}")
                print(f"[votre vie est de {perso.vie} points]")
                print(f"[votre défense est de {perso.défense} points]\n")  
            else:
                print("fuite")
                self.fight_action(ennemy, perso)
                print(ennemy.vie)
        print("le combat est terminé !")
        


    def fight_action(self, ennemy, character):

        if ennemy.défense > 0:
            if ennemy.défense < character.attaque:
                ennemy.vie -= (character.attaque - ennemy.défense)
                ennemy.défense = 0
            else:
                ennemy.défense -= character.attaque
        else:
            if ennemy.défense == 0:
                ennemy.vie -= character.attaque
                if ennemy.vie <= 0:
                    ennemy.vie = 0
            else:
                ennemy.vie -= (character.attaque - ennemy.défense)
        return(ennemy.vie)



