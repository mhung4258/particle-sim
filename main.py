import pygame
import sys
import random
from particle import *
from constants import *
from physics import *
from particle_grid import *

class Simulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("PARTICLE LIFE")
        self.clock = pygame.time.Clock()

        self.particles = [Particle(
            random.randint(PARTICLE_RADIUS, WORLD_WIDTH-PARTICLE_RADIUS),
            random.randint(PARTICLE_RADIUS, WORLD_HEIGHT-PARTICLE_RADIUS)
        ) for _ in range(2000)]
        self.grid = ParticleGrid(cell_size=PARTICLE_RADIUS*3)    
        self.zoom = 1.0
        self.zoom_step = 0.1
        self.min_zoom = 0.2
        self.max_zoom = min(WORLD_WIDTH/WIDTH, WORLD_HEIGHT/HEIGHT)
        self.cam_x = (WORLD_WIDTH - WIDTH /self.zoom)/ 2
        self.cam_y = (WORLD_HEIGHT - HEIGHT/self.zoom)/ 2

        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x = event.pos[0] / self.zoom + self.cam_x
                y = event.pos[1] / self.zoom + self.cam_y
                self.particles.append(Particle(x, y))

            elif event.type == pygame.MOUSEWHEEL:
                mx, my = pygame.mouse.get_pos()

                worldx_pre = mx / self.zoom + self.cam_x
                worldy_pre = my / self.zoom + self.cam_y

                self.zoom += event.y * self.zoom_step
                self.zoom = max(self.min_zoom, min(self.max_zoom, self.zoom))

                self.cam_x = worldx_pre - mx / self.zoom
                self.cam_y = worldy_pre - my / self.zoom

    def update(self):
        handle_all_collisions(self.particles, self.grid)
        apply_interaction(self.particles, self.grid)

        for p in self.particles:
            p.update()
    
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        
        for p in self.particles:
            if(self.cam_x <= p.x <= self.cam_x + WIDTH/self.zoom) and (self.cam_y <= p.y <= self.cam_y +HEIGHT/self.zoom):
                p.draw(self.screen, self.zoom, self.cam_x, self.cam_y) 
        
        
        pygame.draw.rect(self.screen, (128, 128, 128),
            pygame.Rect(
                -self.cam_x * self.zoom,
                -self.cam_y * self.zoom,
                WORLD_WIDTH * self.zoom,
                WORLD_HEIGHT * self.zoom
            ),
            2
        )

        font = pygame.font.SysFont("Arial", 18)
        fps = int(self.clock.get_fps())
        fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))
        self.screen.blit(fps_text, (10, 10))


        p_count = len(self.particles)
        p_count_text = font.render(f"Particles: {p_count}", True, (255, 255, 255))
        self.screen.blit(p_count_text, (10, 30))

        pygame.display.flip()
    
    def move_cam(self):
        keys = pygame.key.get_pressed()
        cam_speed = 10 / self.zoom
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.cam_x -= cam_speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.cam_x += cam_speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.cam_y -= cam_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.cam_y += cam_speed


    def run(self):
        while self.running:
            self.handle_events()
            self.move_cam()
            self.update()
            self.draw()
            self.clock.tick(FPS)


        pygame.quit()
        sys.exit()
    

if __name__ == "__main__":
    sim = Simulation()
    sim.run()

