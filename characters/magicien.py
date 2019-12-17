"""PROJECT RPG DONJONS ET DRAGONS"""

from characters.personnage import Personnage

class Magicien(Personnage):

    def __init__(self, mana):
        super().__init__(150, 40, 50, 20)
        self.mana = 200

