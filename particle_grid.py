class ParticleGrid:
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.grid = {}

    def get_cell_coords(self, x ,y):
        return (int(x // self.cell_size), int(y // self.cell_size))
    
    def update(self, particles):
        self.grid.clear()
        for p in particles:
            cell = self.get_cell_coords(p.x, p.y)
            if cell not in self.grid:
                self.grid[cell] = []
            self.grid[cell].append(p)

    def get_nearby_particles(self, particle):
        nearby = []
        cx, cy = self.get_cell_coords(particle.x, particle.y)

        for dx in [-1,0,1]:
            for dy in [-1, 0, 1]:
                nearby_cell = (cx + dx, cy + dy)
                if nearby_cell in self.grid:
                    nearby.extend(self.grid[nearby_cell])
        nearby = [p for p in nearby if p != particle]

        return nearby