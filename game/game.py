"""game's mechanics"""
from characters.guerrier import Guerrier
from characters.archer import Archer
from characters.thomas_le_méchant import Thomas_le_méchant
from characters.magicien import Magicien
from game.naration import *
import random 
import os

class Game:
    def __init__(self):
        self.nom = None
        self.perso = None
        self.ennemy = None
        self.magicien = Magicien()
        
        
    def player_name(self):
        # One method for the character name
        partie1()
        self.nom= input("Quel est votre nom ? ").upper()
        print(f"Bienvenue {self.nom}, il est temps de prendre votre courage a deux mains !\n")

    def character_choice(self):
        # method that will define self.perso used for the rest of the game
        print("[GUERRIER] |[ARCHER] | [MAGICIEN]\n")
        self.perso = input("Choisissez un aventurier parmis ces trois personnage :" ).lower()
        if self.perso == "guerrier":
            self.perso = Guerrier()
            return self.perso
        elif self.perso == "archer":
            self.perso = Archer()
            return self.perso
        elif self.perso == "magicien":
            self.perso = self.magicien
            return self.perso
        else:
            print("Désolé, je ne connais pas cette aventurier !")
            self.character_choice()
            
    def ennemy_choice(self):
        #only one foe here but with a random instead it work !
        self.ennemy = Thomas_le_méchant()
        print("=============================================================================")
        print("THOMAS LE MÉCHANT ;-( S'APPROCHE DE VOUS ARMÉ DE SA GRANDE RÉGLES ÉPINEUSE !\n--DEUX CHOIX S'OFFRE À VOUS-- ")
        print("sauf si vous jouez magos")
        print("=============================================================================")
        return self.ennemy

    def ennemy_vs_player(self):
        #battle loop, define start en end of the battle + action choices
        self.character_choice()
        partie2()
        self.ennemy_choice()
        while self.perso.vie > 0 and self.ennemy.vie > 0:
            print("[Attaque: A , Fuir: F]")
            if self.perso == self.magicien: #add magician's skill
                print("Se Soigner: S")
            action = input("Que choisissez-vous de faire ? ").lower()
            os.system('clear')
            print("========================================================")
            if action == "a":
                self.fight_action()
                self.fight_action_ennemy()
                print(f"{self.nom} | attaque respectueusement | {self.ennemy.name}")
                print("========================================================")
                print(f"[votre vie est de {self.perso.vie} points]")
                print(f"[votre défense est de {self.perso.défense} points]\n") 
                print(f"[la vie de {self.ennemy.name} est de {self.ennemy.vie} points]")
                print(f"[la défense de Thomas_le_méchant est de {self.ennemy.défense} points]\n")

            if action == "s":
                self.magicien.se_soigner()
            if action == "f":
                self.flee()
                
        partie3()
        print("le combat est terminé, vous avez bien appris !")

    def fight_action(self):
        #based on character's stats, a method for calculating damage and life
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

    def fight_action_ennemy(self):
        #same than fight-action but counter attack from the foe
        if self.perso.défense > 0:
            if self.perso.défense < self.ennemy.attaque:
                self.perso.vie -= (self.ennemy.attaque - self.perso.défense)
                self.perso.défense = 0
            else:
                self.perso.défense -= self.ennemy.attaque
        else:
            if self.perso.défense == 0:
                self.perso.vie -= self.ennemy.attaque
                if self.perso.vie <= 0:
                    self.perso.vie = 0
            else:
                self.perso.vie -= (self.ennemy.attaque - self.perso.défense)
        return(self.perso.vie)

    def flee(self):
        #based on agility stat, modifying the randint modify the chance
        if random.randint(0, 100) in range(0, self.perso.agilité):
            print("Ah tu fuis, j'attend ton mail avec ton lien git-hub !?")
            self.perso.vie = 0
        else:
            print("Reste ici, tu n'as pas commit !")
            self.fight_action_ennemy()


