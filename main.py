from game.game import Game

if __name__ == "__main__":
    
    g = Game()
    g.player_name()
    #print(g.player_name)
    ennemy = g.ennemy_choice()
    character = g.character_choice()
    #print(ennemy,character)
    g.ennemy_vs_player(ennemy, character)
    
    
    

