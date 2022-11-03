# Standard imoprts
import pygame

# Custom imports
import lib
import projectile
import particle
import spells

class Player(pygame.sprite.Sprite):
    def __init__(self, level: object) -> None:
        """Create the player"""

        # Import setup
        pygame.sprite.Sprite.__init__(self) # Initialize the sprite super class
        self.level = level # A reference back to the parent of the player

        # Pos and movement vars
        self.pos = pygame.math.Vector2(int(lib.SCREEN_WIDTH / 2), int(lib.SCREEN_HEIGHT / 2)) # Set the players position to the center of the screen
        self.velo = pygame.math.Vector2() # Create the players velocity vector
        self.speed = 250 # Set the speed variable for the player

        # Fancy things
        self.particleSystem = None # By default we dont get a particle system? TODO make the players particle system work here

        self.spellbook = {
            "Magic Missle": spells.MagicMissle(self.level, "friendly"),
            "Fireball": spells.Fireball(self.level, "friendly")
        }

        self.activeSpell = self.spellbook["Fireball"]

        # Image vars
        self.image = pygame.Surface([40, 40]) # Create the player as a 40x40 square
        self.image.fill(lib.color.WHITE) # Make the player white
        self.image.set_colorkey(lib.color.WHITE) # Make white the colorkey (makes the player ivisible)
        self.rect = self.image.get_rect() # Get the rect of the players image
        self.rect.center = self.pos # Center the rect on the players position

    def update(self) -> None:
        """Update the player"""

        self.pos += self.velo * lib.deltaTime # Position + velocity * delta time = frame independant movement
        self.rect.center = self.pos # Update the center of the rect to the position

        self.move() # Call the players movmement method
        self.interact()
        self.activeSpell.update()

        # Update the particle system
        if self.particleSystem is not None: # If we have a particle system
            self.particleSystem.update(self.pos.x, self.pos.y) # Update it with our latest position

    def interact(self) -> None:
        rawMousePos = pygame.mouse.get_pos()
        worldMousePos = pygame.math.Vector2(rawMousePos[0] + lib.globalOffset.x, rawMousePos[1] + lib.globalOffset.y)

        if pygame.mouse.get_pressed()[0]:
            if self.activeSpell.canBeCast:
                self.activeSpell.castSpell(self.pos.x, self.pos.y, worldMousePos.x, worldMousePos.y)

    def move(self) -> None:
        """Handles player movement based on [WASD] keys"""

        keys = pygame.key.get_pressed() # Get all keys current being pressed

        # Check for horizontal axis
        if keys[pygame.K_a]: # If we find the [A] key
            self.velo.x = -self.speed # Set our horizontal velocity to our negative speed (left)
        elif keys[pygame.K_d]: # If we find the [D] key
            self.velo.x = self.speed # Give our horizontal velocity a postive value instead (right)
        else: # If neither of the horizontal keys are pressed
            self.velo.x = 0 # Kill our velocity

        # Check for vertical axis
        if keys[pygame.K_w]: # If we get the [W] key
            self.velo.y = -self.speed # Set our vertical velocity to negative (up)
        elif keys[pygame.K_s]: # If we get the [S] key
            self.velo.y = self.speed # Set our vertical velocity to positive (down)
        else: # Otherwise
            self.velo.y = 0 # Kill the vertical velocity
