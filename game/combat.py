from characters.guerrier import Guerrier
from characters.archer import Archer
from characters.thomas_le_méchant import Thomas_le_méchant
from characters.magicien import Magicien
from game.naration import *
from game.combat import *
from characters.personnage import Personnage

class Combat(Personnage):

    def attack(self):
            attack = self.perso.attaque - self.ennemy.défense
            return self.ennemy.vie - attack