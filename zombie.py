__author__ = 'Phil'
import pygame
import random
import os

class Zombie:

    def __init__(self):
        self.health = 100
        self.pace = 5
        #placeholder
        self.appearance = self.appearance = pygame.image.load(os.path.join("img","zombie.PNG"))
        self.posX = 0
        self.posY = 0
        self.rect =pygame.Rect(0,0, self.appearance.get_width(), self.appearance.get_height())

    ######################################################
    # spawn the zombie by placing it in a random position
    # with min. 100px distance to the player
    ######################################################
    def spawn(self, playerPos, surface):
        playerX = playerPos.x
        playerY = playerPos.y

        # dont roll the dice if playerX is too close to the left border
        if(playerX < 100):
            horizontal = 1
        else:
            horizontal = random.randint(0,1)

        if(playerY < 100):
            vertical = 1
        else:
            vertical = random.randint(0,1)


        #random X-Position 100px away from the player up to the screen border
        if(horizontal == 1):
            self.posX=random.randint(playerX+100, surface.get_width())
        else:
            self.posX=random.randint(0, playerX-100)

        if(vertical == 1):
            self.posY=random.randint(playerY+100, surface.get_height())
        else:
            self.posY=random.randint(0, playerY-100)

        self.rect.x=self.posX
        self.rect.y=self.posY

        surface.blit(self.appearance, (self.rect.x, self.rect.y))

    ######################################################
    # move the zombie towards the player
    ######################################################
    def move(self, surface):
        surface.blit(self.appearance, (self.rect.x, self.rect.y))
