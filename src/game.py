import asyncio
import enum
import pygame# initilize the pygame module
from pygame.locals import *
import draw
import time
from util import box_states

class map_states(enum.IntEnum):
    INITIALIZE = 0
    BUILD = 1
    UPDATE = 2

class Game(object):
    def __init__(self):
        self.execute_time = 0
        self.running = True

        self.rows, self.cols = (0, 0)
        self.map = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.map_state = map_states.INITIALIZE

        pygame.init()# Setting your screen size with a tuple of the screen width and screen height
        pygame.display.set_caption("RoboFrameworkGFX")# Update your screen when required

        self.surface = pygame.display.set_mode((1920,1080), HWSURFACE|DOUBLEBUF|RESIZABLE)# Setting a random caption title for your pygame graphical window.
        self.work_surface = self.surface.copy()

    async def process_map_data(self, map_data):
        if self.map_state == map_states.INITIALIZE:
            if map_data[0:2] == 'MAP':
                self.rows = int(map_data[3:5])
                self.cols = int(map_data[6:8])
                if self.rows > 1024 or self.cols > 1024:
                    print("Map size too large")
                    return
                if self.rows == 0 or self.cols == 0:
                    print("Map size cannot be 0")
                    return
                self.map = [[0 for i in range(self.cols)] for j in range(self.rows)]
                self.map_state = map_states.BUILDING
            self.map_state = map_states.BUILDING
        elif self.map_state == map_states.BUILDING:
            for i in range(0, len(map_data["boxes"])):
                box = map_data["boxes"][i]
                self.map[box["row"]][box["col"]] = box["state"]
            self.map_state = map_states.UPDATING
        elif self.map_state == map_states.UPDATING:
            for i in range(0, len(map_data["boxes"])):
                box = map_data["boxes"][i]
                self.map[box["row"]][box["col"]] = box["state"]
        else:
            print("Unknown map state")

    async def tick(self, map_data):
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == VIDEORESIZE:
                surface = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)

        process_map_data(map_data)

        draw.map(pygame, self.work_surface, self.matrix)

        self.surface.blit(pygame.transform.scale(self.work_surface, self.surface.get_rect().size), (0, 0))
        pygame.display.update() # quit the pygame initialization and module
        if(self.running == False):
            pygame.quit() # End the program
            quit()