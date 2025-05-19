from constants import *
import numpy as np

def gravity(particle):
    particle.vy += GRAVITY * particle.mass

def edge_detection(particle):

    #Edge Detection
    if particle.x - PARTICLE_RADIUS <= 0:
        particle.vx = abs(particle.vx) * particle.bounce
        particle.x = PARTICLE_RADIUS
    elif particle.x + PARTICLE_RADIUS >= WIDTH:
        particle.vx = -abs(particle.vx) * particle.bounce
        particle.x = WIDTH - PARTICLE_RADIUS

    if particle.y - PARTICLE_RADIUS <= 0:
        particle.vy *= DAMPING
        particle.y = PARTICLE_RADIUS
    elif particle.y + PARTICLE_RADIUS >= HEIGHT:
        particle.vy *= DAMPING
        particle.y = HEIGHT - PARTICLE_RADIUS
        particle.vx *= FLOOR_FRICTION







# Distance formula
def distance_to(particle, other):
    dx = particle.x - other.x
    dy = particle.y - other.y
    return np.sqrt(dx*dx + dy*dy)


