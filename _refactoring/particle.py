# Standard imports
import pygame
import random

# Custom imports
import lib

class Particle(pygame.sprite.Sprite): # The base particle for everyting to happen to, extends the sprite class
    def __init__(self, x: int, y: int, width: int, height: int, color: pygame.Color, minLife: int, maxLife: int) -> None:
        """Create the base particle for particle systems
        
        Arguments:
        x: int - The horizontal position of the particle
        y: int - The vertical position of the particle
        width: int - The width (horizontal) of the particle
        height: int - The height (vertical) of the particle
        color: pygame.Color - The color of the particle
        minLife: int - Minimum physics updates the particle lives for
        maxLife: int - Maximum physics updates the particle lives for
        """
        
        pygame.sprite.Sprite.__init__(self) # Init super class

        # Pos and movement vars
        self.pos = pygame.math.Vector2(x, y) # The position of the particle
        self.velo = pygame.math.Vector2() # The particles movement vectors
        
        self.lifeTime = random.randint(minLife, maxLife) # The random lifetime the particle will live for
        
        # Appearance vars
        self.color = color # The color of the particle
        self.image = pygame.Surface([width, height]) # The size of the particle
        self.image.fill(self.color) # Filling the particle
        self.rect = self.image.get_rect() # Get the particles rect
        self.rect.center = self.pos # Set the center of the rect to the particle pos

    def update(self) -> None:
        """Update the particle"""

        self.pos += self.velo * lib.deltaTime # Update the particle independant of the framerate
        self.rect.center = self.pos # Set the center of the rect to the new particle pos

        self.lifeTime -= 1 # Countdown the particle lifetime
        if self.lifeTime <= 0: # If its out of life
            self.kill() # Kill it

class ParticleSystem():
    def __init__(self, drawContainer: pygame.sprite.Group) -> None:
        """The base particle system, not to be used without extending
        
        Arguments:
        drawContainer: pygame.sprite.Group - The group that will be drawing the particles, passed from subclass
        """
        
        self.drawContainer = drawContainer # The group that draws our particles
        self.particleContainer = pygame.sprite.Group() # Our container for particle physics
        self.particleColor = lib.color.BLACK # The default particle color
        self.maxParticles = 100 # The default for maximum particles

    def createParticles(self, x: int, y: int, count: int, minParticleDim: int, maxParticleDim: int, particleOffset: int, minLife: int, maxLife: int, minVeloX: float, maxVeloX: float, minVeloY: float, maxVeloY: float, minAlpha: int, maxAlpha: int) -> None:
        """Creates the particles used in the particle system (this version should do most of what the old system did, just much more cleanly)
        
        Arguments:
        x: int - The horizontal position of the particle
        y: int - The vertical position of the particle
        count: int - The amount of particles to create
        minParticleDim: int - The minimum size a particle can be
        maxParticleDim: int - The maximum size a particle can be
        particleOffset: int - The number of pixels a particle can be spawned from the (x, y) center of the systme
        minLife: int - The minimum amount of physics updates the particle will live for
        maxLife: int - The maximum amount of physics updates the particle will live for
        minVeloX: float - The minimum speed a particle can have in the horizontal axis
        maxVeloX: float - The maximum speed a particle can have in the horizontal axis
        minVeloY: float - The minimum speed a particle can have in the vertical axis
        maxVeloY: float - The maximum speed a particle can have in the vertical axis
        minAlpha: int - The minimum transparency a particle can have
        maxAlpha: int - The maximum transparency a particle can have
        """
        
        for p in range(count): # Run for as many particles as we need
            particleDim = random.randint(minParticleDim, maxParticleDim) # Get the dimension for this particle
            spawnPos = pygame.math.Vector2(random.randint(x - particleOffset, x + particleOffset), random.randint(y - particleOffset, y + particleOffset)) # Get the random spawn position for this particle, taking offset into account
            p = Particle(spawnPos.x, spawnPos.y, particleDim, particleDim, self.particleColor, minLife, maxLife) # Create the particle

            p.velo.x = random.uniform(minVeloX, maxVeloX) # Assign a random velocity on the horizontal axis
            p.velo.y = random.uniform(minVeloY, maxVeloY) # Assign a random velocity on the vertical axis

            p.image.set_alpha(random.randint(minAlpha, maxAlpha)) # Set a random alpha value to the particle

            self.drawContainer.add(p) # Add the particle to the master draw container
            self.particleContainer.add(p) # Add the particle to our physics container

class PlayerParticleSystem(ParticleSystem): # The players particle system
    def __init__(self, drawContainer: pygame.sprite.Group) -> None:
        """Create a particle system used to represent the player
        
        Arguments:
        drawContainer: pygame.sprite.Group - The master container that will draw the particle system to the screen
        """
        
        super().__init__(drawContainer) # Pass the draw container onto the superclass

        self.spawnPos = pygame.math.Vector2(int(lib.SCREEN_WIDTH / 2), int(lib.SCREEN_HEIGHT / 2)) # Set the spawn postion for the first particles to the center of the screen
        self.particleColor = lib.color.getRandomChoice([lib.color.PLAYER1, lib.color.PLAYER2, lib.color.PLAYER3]) # Get a random particle color from our selections
        self.createParticles(self.spawnPos.x, self.spawnPos.y, self.maxParticles, 3, 5, 15, 20, 45, -40, 40, -40, 40, 25, 255) # Create our particles with the desired behavior

    def update(self, x: int, y: int) -> None:
        """Update the particle system
        
        Arguments:
        x: int - The players new horizontal position
        y: int - The players new vertical position
        """
        
        newPos = pygame.math.Vector2(int(x), int(y)) # Create a vector of the new positions
        self.particleContainer.update() # Update the particles we currently have

        newCount = self.maxParticles - len(self.particleContainer) # Figure out how many particles have died
        self.createParticles(newPos.x, newPos.y, newCount, 3, 5, 15, 20, 45, -40, 40, -40, 40, 25, 255) # Make that many more
