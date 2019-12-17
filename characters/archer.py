"""PROJECT RPG DONJONS ET DRAGONS"""
from characters.personnage import Personnage

class Archer(Personnage):

    def __init__(self, vie, attaque, défense, agilité):
        super().__init__(150, 40, 50, 40)
    