import pygame, sys
from pygame.locals import *

import random

class Runner():
    __customes = ("turtle", "fish", "prawn", "moray", "octopus")
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = "Tortuga"
        
class Game():
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png").convert()
        pygame.display.set_caption("Carrera de bichos")
        
        self.runner = Runner(320, 240)
    
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.runner.position[1] -=5
                        #mover hacia arriba runner
                    elif event.key == K_DOWN:
                        self.runner.position[1] +=5
                        #mover hacia abajo runner
                    elif event.key == K_LEFT:
                        self.runner.position[0] -=5
                        #mover hacia izq runner
                    elif event.key == K_RIGHT:
                        self.runner.position[0] +=5
                        #mover hacia dcha runner
                    else:
                        pass
            #carga pantalla         
            self.__screen.blit(self.__background,(0, 0))
            self.__screen.blit(self.runner.custome, self.runner.position)
        #refresco pantalla
            pygame.display.flip()
    
if __name__ =="__main__":
    game = Game()
    pygame.font.init()
    game.start()