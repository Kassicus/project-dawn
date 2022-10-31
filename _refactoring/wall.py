# Standard imports
import pygame

# Custom imports
import lib

class Wall(pygame.sprite.Sprite): # Extends the sprite class
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        """Create a wall object (sprite)
        
        Arguments:
        x: int - The horizontal position of the wall
        y: int - The vertical position of the wall
        width: int - The width (horizontal) of the wall
        height: int - The height (vertical) of the wall
        """
        
        pygame.sprite.Sprite.__init__(self) # Init superclass

        self.pos = pygame.math.Vector2(x, y) # Create our position
        self.image = pygame.Surface([width, height]) # Create the surface
        self.image.fill(lib.color.BLUE) # Fill the surface for testing TODO add automatic visibility toggle
        self.rect = self.image.get_rect() # Get the rect of the image
        self.rect.topleft = self.pos # Set the rects top left to the position
