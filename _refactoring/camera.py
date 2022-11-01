# Standard imports
import pygame

# Custom imports
import lib

# Custom player centric y-sort camera
class PlayerCenterCamera(pygame.sprite.Group): # Extends the pygame sprite group
    def __init__(self, displaySurface: pygame.Surface, groundSurface: pygame.Surface) -> None:
        """Create an instance of a pygame sprite group with some special features
        
        Arguments:
        displaySurface: pygame.Surface - The main display of the game
        groundSurface: pygame.Surface - The background element of the camera (should be from the level)
        """
        
        pygame.sprite.Group.__init__(self) # INit the superclass\

        # Setup the display
        self.displaySurface = displaySurface # This is what we draw to
        self.halfWidth = self.displaySurface.get_size()[0] // 2 # Get half of the width of the current display (supports resizing)
        self.halfHeight = self.displaySurface.get_size()[1] // 2 # Get half of the height of the current display (supports resizing)

        # Background setup
        self.groundSurface = groundSurface # This is our background for the level
        self.groundRect = self.groundSurface.get_rect(topleft = (0, 0)) # Create a rect for the background so we can move it

    def centerTargetCamera(self, target: pygame.sprite.Sprite) -> None:
        """Get the movement of the player, and move the offsets accordingly
        
        Arguments:
        target: pygame.Sprite - The main game player
        """
        
        # Set offsets
        lib.globalOffset.x = target.rect.centerx - self.halfWidth # Get the offset between the players horizontal pos and the middle of the screen
        lib.globalOffset.y = target.rect.centery - self.halfHeight # Get the offset between the player vertical pos and the middle of the screen

    def cameraDraw(self, player: pygame.sprite.Sprite) -> None:
        """Draw all elements, in a Y sorted fashion, faking depth
        
        Arguments:
        player: pygame.Sprite - The main game player
        """
        
        self.centerTargetCamera(player) # Update the offsets by recentering the camera

        # Ground stuff
        groundOffset = self.groundRect.topleft - lib.globalOffset # Create the offset to draw the ground
        self.displaySurface.blit(self.groundSurface, groundOffset) # Drawn the ground at that offset

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): # Get each sprite in our group, and sort them by the vertical position on screen
            offsetPos = sprite.rect.topleft - lib.globalOffset # Get the offset position for each sprite
            self.displaySurface.blit(sprite.image, offsetPos) # Draw each sprite at the offset position
