import numpy as np
import pygame
import random
from constants import *
from physics import *


class Particle:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.radius = PARTICLE_RADIUS
        self.color = random.choice(PARTICLE_COLORS)
        self.vx = random.uniform(-5,5)
        self.vy = random.uniform(-5,5)
        self.mass = 0.3 #random.uniform(0.8, 1.2)
        self.bounce = random.uniform(0.7, 0.9)

    def update(self):
        gravity(self)
        #update position by velocity
        self.x += self.vx 
        self.y += self.vy
        
        if abs(self.vx) < MINIMUM_VELOCITY:
            self.vx *= 0.5
        if abs(self.vy) < MINIMUM_VELOCITY:
            self.vx *= 0.5
        edge_detection(self)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color,(self.x, self.y), self.radius)

    