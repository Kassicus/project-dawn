# Standard library imports
import pygame

_projectiles = pygame.sprite.Group() # Python handles sprites in groups, this is for organization purposes

# Generic projectile class (Currently does no damage, as we have no enemies yet)
class Projectile(pygame.sprite.Sprite): # Extends the default python sprite class
    def __init__(self, origin_x, origin_y, direction, size, speed, color, psystem=None): 
        """
        direction: the self.facing value of the entity creating the projectile
        """

        pygame.sprite.Sprite.__init__(self) # Initializing the sprite parent class

        # Position variables
        self.x = origin_x
        self.y = origin_y
        self.pos = (self.x, self.y)

        # Velocity control
        self.x_velocity = 0
        self.y_velocity = 0
        self.speed = speed

        # Determines the initial velocity of the projectile by what player facing orientation was provided
        if direction == "left":
            self.x_velocity = -self.speed
        elif direction == "right":
            self.x_velocity = self.speed
        elif direction == "away":
            self.y_velocity = -self.speed
        elif direction == "forward":
            self.y_velocity = self.speed

        # Generic variables
        self.size = size
        self.color = color

        # To be implemented
        self.psystem = psystem

    # Dirty fix to use in place of the generic draw function built into sprites
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.size, 0)

    # Handles all non-graphical events and updates
    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

        self.pos = (self.x, self.y)

        self.check_overrun() # memory control

    # Specifically checks if the projectile is outside of the screen (kills if it is)
    def check_overrun(self):
        if self.x < -100 or self.x > 1100:
            self.kill()
        
        if self.y < -100 or self.y > 900:
            self.kill()
