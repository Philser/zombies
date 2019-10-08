__author__ = 'Phil'

import pygame, sys
from pygame.locals import *
import playerClass
import Shot
import time
import zombie




class App:

    WINDOWWIDTH = 1440
    WINDOWHEIGHT = 900


    def __init__(self):
        self._running = True
        self.displaysurf = None
        self.player = None
        self.playerAppearance = None

        self.playerX = 0
        self.playerY = 0

        self.playerWidth = 0
        self.playerHeight = 0

        self.fpsClock = None
        self.FPS = 0
        self.lineColor = None
        self.pressed_up = None
        self.pressed_down = None
        self.pressed_right = None
        self.pressed_left = None
        self.pressed_lmouse = None
        self.shotList = None

        self.ZOMBIESPAWN = None
        self.zombieEvent = None

        self.zombieList = None
        self.ticks = 0

    ####################################
    # initialize
    ####################################
    def on_init(self):
        pygame.init()
        self.displaysurf = pygame.display.set_mode((self.WINDOWWIDTH,self.WINDOWHEIGHT))
        pygame.display.set_caption("Window Caption")

        #player related stuff
        self.player = playerClass.Player()
        self.playerAppearance = self.player.appearance



        self.playerWidth = self.playerAppearance.get_width()
        self.playerHeight = self.playerAppearance.get_height()

        self.fpsClock = pygame.time.Clock()
        self.FPS=60
        self.lineColor = (255,0,0)
        self.pressed_up = False
        self.pressed_down = False
        self.pressed_right = False
        self.pressed_left = False
        self.pressed_lmouse = False
        self.shotList = []

        #event for spawning zombies by timer
        #use post to add event to the queue for the first time
        self.ZOMBIESPAWN = USEREVENT + 1
        self.zombieEvent = pygame.event.Event(self.ZOMBIESPAWN)
        pygame.event.post(self.zombieEvent)
        #zombie spawn clock
        pygame.time.set_timer(self.zombieEvent.type, 1000)
        self.zombieList = []

        self._running = True

    def on_loop(self):
        pass

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
            
        while self._running:
            #
            # event handling loop
            #          

            for event in pygame.event.get():
                    if event.type == pygame.locals.QUIT:
                        pygame.quit()
                        sys.exit()

                    #handling keyboard input
                    #start moving
                    if event.type == pygame.locals.KEYDOWN:
                        if event.key == pygame.locals.K_w:
                            self.pressed_up = True
                        if event.key == pygame.locals.K_d:
                            self.pressed_right = True
                        if event.key == pygame.locals.K_s:
                            self.pressed_down = True
                        if event.key == pygame.locals.K_a:
                            self.pressed_left = True
                    #stop moving
                    elif event.type == pygame.locals.KEYUP:
                        if event.key == pygame.locals.K_w:
                            self.pressed_up = False
                        if event.key == pygame.locals.K_d:
                            self.pressed_right = False
                        if event.key == pygame.locals.K_s:
                            self.pressed_down = False
                        if event.key == pygame.locals.K_a:
                            self.pressed_left = False

                    #handling mouse input
                    #looking around / aiming
                    elif event.type == pygame.MOUSEMOTION:
                        mousePos = event.pos
                    #firing
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                        self.pressed_lmouse = True
                        mousePos = event.pos
                        shot = Shot.Shot(mousePos, self.player.getPosition())
                        self.shotList.append(shot)
                        self.lineColor = (0,0,255)

                    elif event.type == pygame.MOUSEBUTTONUP and event.button==1:
                        self.pressed_lmouse = False
                        mousePos = event.pos
                        self.lineColor = (255,0,0)

                    #spawning zombies
                    if event.type == self.ZOMBIESPAWN:
                        newZombie = zombie.Zombie()
                        self.zombieList.append(newZombie)
                        newZombie.spawn(self.player.getPosition(), self.displaysurf)
                        print("Zombie spawned")
            #
            # moving the player
            #
            if self.pressed_up:
                if self.player.getPosition().top>0:
                    self.player.move(0, -self.player.pace)
            if self.pressed_right:
                if self.player.getPosition().right<self.WINDOWWIDTH- self.player.pace:
                    self.player.move(self.player.pace, 0)
            if self.pressed_down:
                if self.player.getPosition().bottom<self.WINDOWHEIGHT- self.player.pace:
                    self.player.move(0, self.player.pace)
            if self.pressed_left:
                if self.player.getPosition().left>0:
                    self.player.move(-self.player.pace, 0)




            #
            # render
            #
            self.displaysurf.fill((255,255,255))

            pygame.draw.line(self.displaysurf, self.lineColor, (
            self.player.getPosition().left+ self.player.appearance.get_width()/2, self.player.getPosition().top+ self.player.appearance.get_height()/2), mousePos)

            #
            # checking shot collision
            #
            for shot in self.shotList:

                #checking if the shot is out of the screen
                if shot.isOutOfScreen(self.WINDOWWIDTH, self.WINDOWHEIGHT):
                    self.shotList.remove(shot)
                    print("deleting shot")
                else:
                    shot.move(self.displaysurf)

                # good style? (regarding the different data types in a single return statement)

                #checking if the shot is hitting a zombie
                collisionArray = shot.collisionCheck(self.zombieList)
                if collisionArray[0] == True:
                    self.shotList.remove(shot)
                    self.zombieList = collisionArray[1]
                    print("deleting shot")
            #
            # zombie spawner
            #
            for zomb in self.zombieList:
                zomb.move(self.displaysurf)

            self.player.draw(self.displaysurf)
            self.fpsClock.tick(self.FPS)
            pygame.display.update()


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

