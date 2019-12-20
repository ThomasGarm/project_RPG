"""PROJECT RPG DONJONS ET DRAGONS"""

from characters.personnage import Personnage

class Magicien(Personnage):

    def __init__(self, mana):
        super().__init__(600, 20, 50, 25)
        self.mana = 200

    def cast(self, mana, vie):
        heal = (input("Se soigner : S")).lower()
        if heal == "s":
            self.mana -= 50
            self.vie += 100



