
from personnage import Personnage
class Thomas_le_méchant(Personnage):
    def __init__(self, vie, attaque, défense, agilité, nom):
        super().__init__(500, 100, 50, 10, nom)