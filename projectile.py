# Standard library imports
import pygame
import math

# Custom imports
import reference
import sound

# Master groups
_projectiles = pygame.sprite.Group() # Acts as a global container for all projectiles, can be passed and refernced by other files

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, tx, ty, width, height, particleSystem, speed, soundFile):
        """Dynamic projectile, capable of being created by anything
        
        Keyword arguments:
        x (int) : The horizontal position of the projectile
        y (int) : The vertical position of the projectile
        tx (int) : The hortizontal target position
        ty (int) : The vertical target position
        width (int) : The width of the projectile
        height (int) : The height of the projectile
        particleSystem (object) : Optional particle system to make fun bullet trail bullshit
        speed (int) : The speed of the bullet
        """
        
        pygame.sprite.Sprite.__init__(self) # Initialize the super class

        # Position and velocity
        self.pos = pygame.math.Vector2(x, y) # Vector to contain the x and y
        self.velocity = pygame.math.Vector2() # Vector to contain x and y change in velocity
        self.target = pygame.math.Vector2(tx, ty) # Vector to contain the targets x and y

        # Dimension variables
        self.width = width # Width of the projectile
        self.height = height # Height of the projectile

        self.particleSystem = particleSystem # Particle system

        self.speed = speed # Projectile speed

        # Image and drawing variables
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(reference.WHITE)
        self.displaySurface = pygame.display.get_surface()
        self.rect = self.pos

        # Get velocities
        self.velocity.x = self.getVectors()[0] # Set the x velocity based on the getVectors() function
        self.velocity.y = self.getVectors()[1] # Set the y velocity based ont the getVectors() function

        if soundFile is not None:
            sound.playSound(soundFile)

    def getVectors(self):
        """Takes the spawn position and target position and does fancy math to move the bullet"""

        distance = [self.target.x - self.pos.x, self.target.y - self.pos.y] # Difference in the x values and difference in the y values
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2) # This is just pythagorean theorum. A^2 + B^2 = C^2, but for us its C = sqrt(A^2 + B^2)
        direction = [distance[0] / normal, distance[1] / normal] # Divide the difference by the normal to get a rise over run step
        vectors = [direction[0] * self.speed, direction[1] * self.speed] # Multiply that step by speed to get the actual change in rise over run for the projectile

        return vectors # Return those projectiles

    def update(self):
        """Update the projectile"""

        # Particle system update
        self.particleSystem.draw(self.displaySurface) # Draw the particle system to
        self.particleSystem.update() # Update the particle system

        self.pos += self.velocity * reference.dt # Add the velocity to the position with delta time

        self.rect = self.pos # Update the rect (top-left) to the position

        self.particleSystem.pos = self.pos # Update the root of the particle system to follow the projectile

        self.checkOverrun() # Check the overrun of the projectile on the map

    def checkOverrun(self):
        """If for whatever reason we leave the screen, kill the projectile"""

        if self.pos.x < -500 or self.pos.x > 1500: # If we are outside of the screen horizontally
            self.kill() # Kill the projectile
        
        if self.pos.y < -500 or self.pos.y > 1300: # If we are outside of the screen vertically
            self.kill() # Kill the projectile
