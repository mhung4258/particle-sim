from constants import *
import numpy as np
from particle_grid import *


def edge_detection(particle):

    #Edge Detection
    if particle.x - particle.radius <= 0:
        particle.vx = abs(particle.vx) * particle.bounce
        particle.x = particle.radius
        if abs(particle.vx) < MINIMUM_VELOCITY:
            particle.vx *= .5

    elif particle.x + particle.radius >= WORLD_WIDTH:
        particle.vx = -abs(particle.vx) * particle.bounce
        particle.x = WORLD_WIDTH - particle.radius
        if abs(particle.vx) < MINIMUM_VELOCITY:
            particle.vx *= .5

    if particle.y - particle.radius <= 0:
        particle.vy = abs(particle.vy) * particle.bounce
        particle.y = particle.radius
        if abs(particle.vy) < MINIMUM_VELOCITY:
            particle.vy *= .5

    elif particle.y + particle.radius >= WORLD_HEIGHT:
        particle.vy = -abs(particle.vy) * particle.bounce
        particle.y = WORLD_HEIGHT - particle.radius
        if abs(particle.vy) < MINIMUM_VELOCITY:
            particle.vy *= .5
        particle.vx *= FLOOR_FRICTION


# Distance formula
def distance_to(particle, other):
    dx = particle.x - other.x
    dy = particle.y - other.y
    return np.sqrt(dx*dx + dy*dy)

def check_collision(p1,p2):
    return distance_to(p1,p2) < (p1.radius + p2.radius)

def collission_handler(p1,p2):
    # calculate the collision direction
    distance= max(0.1, distance_to(p1,p2))
    nx = (p2.x - p1.x) / distance
    ny = (p2.y - p1.y) /distance

    #Velocity of the hit
    rvx = p2.vx - p1.vx
    rvy = p2.vy - p1.vy

    velocity = (rvx*nx) + (rvy * ny)

    # Don't resolve if separating
    if velocity > 0:
        return
    
    #Impulse
    avg_bounce = (p1.bounce + p2.bounce)/2
    impulse = -(1 + avg_bounce) * velocity
    impulse /= 1/p1.mass + 1/p2.mass

    #Rebound
    ix = impulse * nx
    iy = impulse * ny


    p1.vx -= ix / p1.mass
    p1.vy -= iy / p1.mass
    p2.vx += ix / p2.mass
    p2.vy += iy / p2.mass
    
    ##Overlap Handler
    overlap = (p1.radius + p2.radius) - distance
    if overlap > 0:
        separation = overlap * 0.8
        p1.x -= separation * nx * 0.5
        p2.x += separation * nx * 0.5
        p1.y -= separation * ny * 0.5
        p2.y += separation * ny * 0.5

# accepts list of particles
def handle_all_collisions(particles, grid):
    grid.update(particles)

    for particle in particles:
        nearby = grid.get_nearby_particles(particle)

        for other in nearby:
            if particle != other and check_collision(particle, other):
                collission_handler(particle, other)
    
# Interations for Particle Life

def apply_interaction(particles, grid):
    grid.update(particles)
    for p in particles:
        nearby = grid.get_nearby_particles(p)

        for other in nearby:
            if p is other:
                continue

            dx = other.x - p.x
            dy = other.y - p.y

            dist_sq = dx * dx + dy * dy
            dist_sq = max(0.01,  dist_sq)
            dist = max(1.0, np.sqrt(dist_sq)) 

            if dist > 100:
                continue

            force = INTERACTION_RULES[p.type][other.type]
            strength = force / dist_sq
            fx = strength * dx
            fy = strength * dy

            p.vx += fx
            p.vy += fy
