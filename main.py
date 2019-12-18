from game.game import Game
from characters.guerrier import Guerrier
from characters.archer import Archer
from characters.personnage import Personnage

if __name__ == "__main__":
    
    game = Game()
    game.player_name()
    
    game.ennemy_vs_player()
    print(game.guerrier.vie)
    print(game.ennemy)
    print(game.character_choice)
    game.test()
    
    
    
    
    
    

