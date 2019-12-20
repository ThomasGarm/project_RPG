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
        
        
    def player_name(self):
        partie1()
        self.nom= input("Quel est votre nom ? ").upper()
        print(f"Bienvenue {self.nom}, il est temps!\n")

    def character_choice(self):
        print("[GUERRIER] |[ARCHER] | [MAGICIEN]\n")
        self.perso = input("Choisissez un aventurier parmis ces trois personnage :" ).lower()
        if self.perso == "guerrier":
            self.perso = Guerrier()
            return self.perso
        elif self.perso == "archer":
            self.perso = Archer()
            return self.perso
        elif self.perso == "magicien":
            self.perso = Magicien()
            return self.perso
        else:
            print("Désoler, je connais pas cette aventurier !")
            self.character_choice()
            
    def ennemy_choice(self):
        self.ennemy = Thomas_le_méchant()
        print("THOMMAS LE MÉCHANT ;-( S'APPROCHE DE VOUS ARMÉ DE SA GRANDE RÉGLES ÉPINEUSE !\n--DEUX CHOIX S'OFFRE À VOUS-- ")
        return self.ennemy

    def ennemy_vs_player(self):
        self.character_choice()
        self.ennemy_choice()
        while self.perso.vie > 0 and self.ennemy.vie > 0:
            print("[Attaque: A , Fuir: F]")
            action = input("Que choisissez-vous de faire ? ").lower()
            if action == "a":
                self.fight_action()
                print(f"{self.nom} | attaque violamment | {self.ennemy.name}\n")
                print(f"[votre vie est de {self.perso.vie} points]")
                print(f"[votre défense est de {self.perso.défense} points]\n") 
                print(f"[la vie de {self.ennemy.name} est de {self.ennemy.vie} points]")
                print(f"[la défense de Thomas_le_méchant est de {self.ennemy.défense} points]\n")   
            else:
                action == "f"
                self.fight_action()
                print(f"{self.nom} | tente de fuir | {self.ennemy.name}\n")
                print(f"[la vie de {self.ennemy.name} est de {self.ennemy.vie} points]")
                print(f"[la défense de Thomas_le_méchant est de {self.ennemy.défense} points]\n")
                print(f"[votre vie est de {self.perso.vie} points]")
                print(f"[votre défense est de {self.perso.défense} points]\n") 

        print("le combat est terminé !")
        

    def fight_action(self):
        if self.ennemy.défense > 0:
            if self.ennemy.défense < self.perso.attaque:
                self.ennemy.vie -= (self.perso.attaque - self.ennemy.défense)
                self.ennemy.défense = 0
            else:
                self.ennemy.défense -= self.perso.attaque
        else:
            if self.ennemy.défense == 0:
                self.ennemy.vie -= self.perso.attaque
                if self.ennemy.vie <= 0:
                    self.ennemy.vie = 0
            else:
                self.ennemy.vie -= (self.perso.attaque - self.ennemy.défense)
        return(self.ennemy.vie)



