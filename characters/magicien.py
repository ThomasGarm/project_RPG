"""PROJECT RPG DONJONS ET DRAGONS"""
from characters.personnage import Personnage

class Magicien(Personnage):
    mana = 200

    def __init__(self):
        super().__init__(150, 40, 50, 20)
    