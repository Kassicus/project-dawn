import pygame
import math

import lib
import sound

class Projectile(pygame.sprite.Sprite):
    def __init__(
        self,
        x: int,
        y: int,
        targetX: int,
        targetY: int,
        size: int,
        speed: float,
        trailParticleSystem: object,
        explodes: bool,
        explosionParticleSystem: object,
        drawContainer: pygame.sprite.Group,
        damage: int,
        spawnSound: str
    ) -> None:
        
        """Create a projectile
        
        Arguments:
        x: int - The initial horizontal posision of the projectile
        y: int - The initial vertical position of the projectile
        targetX: int - The intended horizontal position of the projectile
        targetY: int - The intended vertical position of the projectile
        size: int - The amount of pixels the projectile is wide and tall
        speed: float - The speed of the projectile
        particleSystem: object - The particle system of the projectile
        drawContainer: pygame.sprite.Group - The levels main camera object
        damage: int - The amount of damage the projectile will do to enemies
        spawnSound: str - The dictionary key of the desired sound to be played when the projectile is created
        """
        
        super().__init__()

        self.pos = pygame.math.Vector2(x, y) # Vector for our current position
        self.velo = pygame.math.Vector2() # Vector for our movement
        self.targetPos = pygame.math.Vector2(targetX, targetY) # Vector for the target position
        self.speed = speed # How fast we get to our target position
        self.damage = damage # The amount of damage we do
        self.lifetime = 8000 # The default lifetime of the projectile (this is here in case a particle makes it outside the map at all)
        self.explodes = explodes

        sound.playSound(spawnSound) # Play the spawn sound on init

        self.trailParticleSystem = trailParticleSystem(self.pos.x, self.pos.y) # Create our particle system
        self.explosionParticleSystem = explosionParticleSystem

        self.image = pygame.Surface([size, size]) # Create a square surface for our image
        self.image.fill(lib.color.WHITE) # Fill that surface solid white
        self.rect = self.image.get_rect() # Get the rect of the surface
        self.rect.center = self.pos # Set the center of the rect to the projectile position

        self.velo.x = self.getVectors()[0] # Map our x movement to our first vector
        self.velo.y = self.getVectors()[1] # Map our y movement to our second vector

    def getVectors(self) -> list:
        """Takes the spawn position and target position and does fancy math to get the bullet vectors
        
        Returns:
        vectors: list - The calculated vectors [0] = x, [1] = y
        """

        distance = [self.targetPos.x - self.pos.x, self.targetPos.y - self.pos.y] # Difference in the x values and difference in the y values
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2) # This is just pythagorean theorum. A^2 + B^2 = C^2, but for us its C = sqrt(A^2 + B^2)
        direction = [distance[0] / normal, distance[1] / normal] # Divide the difference by the normal to get a rise over run step
        vectors = [direction[0] * self.speed, direction[1] * self.speed] # Multiply that step by speed to get the actual change in rise over run for the projectile

        return vectors # Return those vectors

    def explode(self) -> None:
        if self.explodes:
            e = self.explosionParticleSystem(self.pos.x, self.pos.y)
            lib.levelref.worldCamera.add(e)
            lib.levelref.particles.add(e)

    def destroy(self) -> None:
        self.explode()
        self.kill()

    def update(self) -> None:
        """Update the projectile"""

        self.pos += self.velo * lib.deltaTime # Move the projectile
        self.rect.center = self.pos # Set the center of the rect to the new position

        if self.trailParticleSystem is not None: # If we have a particle system
            self.trailParticleSystem.update(self.pos.x, self.pos.y) # Make sure to update it

        self.lifetime -= 1 # Count down our lifetime (kinda range?)
        if self.lifetime <= 0: # If it runs out
            self.kill() # We die