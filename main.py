import pygame, sys
import random

class Runner():
    __customes = ("turtle", "fish", "prawn", "moray", "octopus")
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = "Tortuga"

    def avanzar(self):
        self.position[0] += random.randint(1, 6)
        

class Game():
    runners = []
    __posY = (160, 200, 240, 280)
    __names = ("Speedy", "Lucera", "Alonso", "Torcuata")
    __startLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png").convert()
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range (4):
            
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
        self.runners.append(theRunner)
        
    def close(self):
        pygame.quit()
        sys.exit()
    
    def competir(self):  
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
        
            self.runners[0].avanzar()
            
            if self.runners[0].position[0] >= self.__finishLine:
                print("{} ha ganado". format(self.runners[0].name))
                gameOver = True
            
            self.__screen.blit(self.__background,(0, 0))
           
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
        
            pygame.display.flip()
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
    
        pygame.quit()
        sys.exit()
        
if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()