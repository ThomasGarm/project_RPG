from characters.personnage import Personnage

class Thomas_le_méchant(Personnage):
    
    def __init__(self):
        super().__init__(400, 40, 70, 20)
        self.name = "Thomas_le_méchant"
        
    def __repr__(self):
        return super().__repr__()
    