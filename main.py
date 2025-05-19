import pygame
import sys
import random
from particle import *
from constants import *
from physics import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Particle Simulation")
    clock = pygame.time.Clock()
    
    particles = [Particle(
        random.randint(PARTICLE_RADIUS, WIDTH-PARTICLE_RADIUS),
        random.randint(PARTICLE_RADIUS, HEIGHT//2)
    ) for _ in range(100)]

    
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                particles.append(Particle(x, y))

        for p in particles:
            p.update()
            p.draw(screen)
        


        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()