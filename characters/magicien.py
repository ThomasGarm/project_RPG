"""PROJECT RPG DONJONS ET DRAGONS"""

from characters.personnage import Personnage

class Magicien(Personnage):

    def __init__(self):
        super().__init__(600, 20, 50, 25)
        self.mana = 200

    def cast(self):
        self.mana -= 50
        self.vie += 100 
        print(f"Il vous reste {self.mana} mana et votre vie remonte à {self.vie}")
        if self.mana == 0:
            print("Vous ne pouvez plus vous soigner.")



