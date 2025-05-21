WIDTH, HEIGHT = 1600, 1080
WORLD_WIDTH, WORLD_HEIGHT = 3000, 3000

FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
PARTICLE_RADIUS = 3
MAXIMUM_VELOCITY = 1
MINIMUM_VELOCITY = 0.01

FLOOR_FRICTION = 0.9
BOUNCE = 0.5

NUM_TYPE = 4
PARTICLE_COLORS = [
    (100, 255, 100),  # Prey - Green
    (255, 80, 80),    # Predator - Red
    (80, 80, 255),    # Neutral - Blue
    (255, 255, 100),  # Social - Yellow
]


# INTERACTION_RULES = [
#     [ 0.0,  0.5, -0.4,  0.2],
#     [-0.3,  0.0,  0.6, -0.1],
#     [ 0.2, -0.2,  0.0,  0.8],
#     [ 0.1,  0.3, -0.3,  0.0]
# ]


# INTERACTION_RULES = [
#     [ 0.5, 0.0, 0.0, 0.0],
#     [ 0.0, 0.5, 0.0, 0.0],
#     [ 0.0, 0.0, 0.5, 0.0],
#     [ 0.0, 0.0, 0.0, 0.5]
# ]

INTERACTION_RULES = [
    #   G       R     B       Y    
    [  0.0,  -1.0,   0.3,    0.8],   #G
    [  1.0,  -0.5,  -0.2,   -0.1],   #R
    [ -0.2,  -0.2,   0.0,    0.4],   #B
    [  0.5,  -0.1,   0.5,    0.7]    #Y
]