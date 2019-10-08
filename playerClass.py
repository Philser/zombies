import pygame
import os

class Player:

    def __init__(self):
        self.health = 100
        self.lifes = 1
        self.pace = 5
        self.appearance = pygame.image.load(os.path.join("img","player.png"))
        self.posX = 0
        self.posY = 0
        self.rect = pygame.Rect(0,0, self.appearance.get_width(), self.appearance.get_height())
        self.direction = ''

    ######################################################
    # draw the graphics
    ######################################################
    def draw(self, surface):
        surface.blit(self.appearance, (self.rect.left, self.rect.top))

    ######################################################
    # move the player
    ######################################################
    def move(self, x, y):
        self.rect = self.rect.move(x,y)

    ######################################################
    # returns the position of the player's rectangle
    ######################################################
    def getPosition(self):
        return self.rect

