import numpy as np
import pygame
import random
from constants import *
from physics import *


class Particle:
    def __init__(self, x ,y, type=None):
        self.x = x
        self.y = y
        self.radius = PARTICLE_RADIUS
        self.vx = 0
        self.vy = 0
        self.mass = 0.3 
        self.bounce = 0.8
        self.type = type if type is not None else random.randint(0, NUM_TYPE - 1)
        self.color = PARTICLE_COLORS[self.type]


    def update(self):
        #update position by velocity
        self.x += self.vx 
        self.y += self.vy

        speed = np.hypot(self.vx, self.vy)
        if speed > MAXIMUM_VELOCITY:
            scale = MAXIMUM_VELOCITY / speed
            self.vx *= scale
            self.vy *= scale
        
        if abs(self.vx) < MINIMUM_VELOCITY:
            self.vx *= 0.5
        if abs(self.vy) < MINIMUM_VELOCITY:
            self.vx *= 0.5
        edge_detection(self)
    
    def draw(self, screen, zoom, cam_x, cam_y):
        draw_x = int((self.x - cam_x)* zoom)
        draw_y = int((self.y - cam_y) * zoom)
        draw_radius = max(1, int(self.radius * zoom))


        pygame.draw.circle(screen, self.color,(draw_x,draw_y), draw_radius)

    