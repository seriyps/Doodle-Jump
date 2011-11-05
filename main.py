#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys

from locations import *
from sprites import *


# Main class for game window
class Game():
    level = 0

    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode((480, 640))
        pygame.display.set_caption('Doodle jump')
    def event(self, event):
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                if isinstance(self.location, GameLocation):
                    self.location = StartLocation(self)
                elif isinstance(self.location, StartLocation):
                    sys.exit()
                

# main function
def main():
    game = Game()

    start_location = StartLocation(game)

    game.location = start_location

    clock = pygame.time.Clock()
    while 1:
        clock.tick(45)
        game.location.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            game.location.event(event)
            game.event(event)            
            
    
if __name__ == "__main__":
    main()
