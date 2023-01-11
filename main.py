import pygame, sys

class Ship(pygame.sprite.Sprite):
    def __init__(self,groups):
        # 1. We have to init the parent class
        super().__init__(groups)
        
        # 2. We need a surface
        self.image = pygame.image.load('./graphics/ship.png').convert_alpha()
        
        # 3. We need a rect
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        
# basic setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

# background
background_surf = pygame.image.load('./graphics/background.png').convert()

# sprite groups
spaceship_group = pygame.sprite.Group()

# sprite creation
ship = Ship(spaceship_group)

# main game loop
while True:
    
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # delta time
    dt = clock.tick() / 1000
    
    display_surface.blit(background_surf, (0, 0))
    
    # graphics
    spaceship_group.draw(display_surface)
    
    # draw the frame
    pygame.display.update()
    
    