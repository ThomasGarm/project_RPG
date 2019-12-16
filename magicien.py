"""PROJECT RPG DONJONS ET DRAGONS"""

class Magicien(Personnage):

    def __init__(self, vie, attaque, défense, agilité, nom, mana):
        super().__init__(150, 40, 50, nom, 200)
    