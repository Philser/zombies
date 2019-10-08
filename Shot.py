import pygame
import math

class Shot:


    def __init__(self, mousePos, playerPos):
        self.speed = 50
        self.direction = []

        self.mousePos = mousePos
        self.playerPos = playerPos

        self.image = pygame.Surface([3, 3])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = playerPos.x + (playerPos.width / 2)
        self.rect.y = playerPos.y + (playerPos.height / 2)

    ######################################################
    # move the shot
    ######################################################
    def move(self, surface):

        distance = [self.mousePos[0] - self.playerPos[0], self.mousePos[1] - self.playerPos[1]]
        norm = math.sqrt( distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / norm, distance[1] / norm]
        bullet_vector = [direction[0] *self.speed, direction[1] * self.speed]

        self.rect.x += bullet_vector[0]
        self.rect.y += bullet_vector[1]
        surface.blit(self.image, (self.rect.x, self.rect.y))

    ######################################################
    # check if the shot collides with a zombie
    # returns the zombieList without the collided zombies
    ######################################################
    def collisionCheck(self, zombieList):
        isCollided = False
        for zombie in zombieList:
            #collision check
            #check if the X and Y of the shot is between the zombie rectangle WIDTH and HEIGHT
            #@NOTE: DOUBLECHECK IF THIS CONDITION IS TRUE ONLY FOR ACTUALLY HIT ZOMBIES AND NOTHING ELSE
            #if( (self.rect.x - zombie.rect.x) > (zombie.rect.x-zombie.rect.right) and (self.rect.x - zombie.rect.x) < (zombie.rect.x+zombie.rect.right) and (self.rect.y -zombie.rect.y) > (zombie.rect.y-zombie.rect.bottom) and (self.rect.y-zombie.rect.y) < (zombie.rect.y+zombie.rect.bottom) ):
             if(
                    #shot is coming from the left
                ((self.rect.x < zombie.rect.x + zombie.rect.width and self.rect.x + self.rect.width >= zombie.rect.x) or
                    #shot is coming from the right
                (self.rect.x <= zombie.rect.x + zombie.rect.width and self.rect.x + self.rect.width > zombie.rect.x + zombie.rect.width))
                and
                    #shot is coming from above
                ((self.rect.y < zombie.rect.y + zombie.rect.height and self.rect.y + self.rect.height >= zombie.rect.y) or
                    #shot is coming from below
                (self.rect.y <= zombie.rect.y + zombie.rect.height and self.rect.y + self.rect.height > zombie.rect.y + zombie.rect.height))

             ):
                zombieList.remove(zombie)
                print("Zombie killed.")
                print("Zombie Coords: " + str(zombie.rect.x) + "-" + str(zombie.rect.right) + " " + str(zombie.rect.y) + "-" + str(zombie.rect.bottom))
                print("Shot Coords: " + str(self.rect.x) + "-" + str(self.rect.right) + " " + str(self.rect.y) + "-" + str(self.rect.bottom))
                isCollided = True
                break

        return [isCollided, zombieList]

    ######################################################
    # check if the shot is out of the screen
    ######################################################
    def isOutOfScreen(self, borderX, borderY):
        if self.rect.x > borderX or self.rect.y > borderY or self.rect.x < 0 or self.rect.y < 0:
            return True
        else:
            return False