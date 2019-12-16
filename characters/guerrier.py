
from personnage import Personnage
class Guerrier(Personnage):
    def __init__(self, vie, attaque, défense, agilité, nom):
        super().__init__(500, 100, 50, 10, nom)
