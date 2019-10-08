__author__ = 'Phil'

def collisionCheck(shot, zombieList):
        for zombie in zombieList:
            #collision check
            #check if the X and Y of the shot is between the zombie rectangle WIDTH and HEIGHT
            if( (shot.rect.x - zombie.rect.x) > (zombie.rect.x-zombie.rect.right) and (shot.rect.x - zombie.rect.x) < (zombie.rect.x+zombie.rect.right) and (shot.rect.y -zombie.rect.y) > (zombie.rect.y-zombie.rect.top) and (shot.rect.y-zombie.rect.y) < (zombie.rect.y+zombie.rect.top) ):
                zombieList.remove(zombie)
                print("Zombie killed")
        return zombieList