# Standard library imports
from weakref import ref
import pygame
import random

# Custom imports
import reference

# Particle class, extends sprite. Uses sprite drawing method (image/surface based)
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, minLife, maxLife, decays=True):
        """The base particle used in the particle systems
        
        Keyword arguments:
        x (int) : The horizontal position of the particle
        y (int) : The vertical position of the particle
        width (int) : The width of the particle
        height (int) : The height of the particle
        color (tuple) : The rgb color of the particle
        minLife (int) : The minimum amount of updates that the particle lives for
        maxLife (int) : The maximum amount of updates that the particle lives for
        decays (boolean) : Determines if the particle decays (default=True)
        """
        
        pygame.sprite.Sprite.__init__(self) # Initialize super class

        # Position variables
        self.pos = pygame.math.Vector2(x, y) # Vector to contain the particle x and y
        self.velocity = pygame.math.Vector2() # Vector to contain the velocity change in x and y

        # Facade variables
        self.activeFacade = False # Determines if the particles uses a facade
        self.facadeType = "" # Type of facade used
        self.facadeWidth = 0 # Facade width
        self.facadeHeight = 0 # Facade height
        self.facadeRadius = 0 # Facade radius (if circle)
        self.facadeColor = (0, 0, 0) # Facade color

        # Dimension variables
        self.width = width # Particle width
        self.height = height # Particl height

        # Lifetime variables
        self.lifetime = random.randint(minLife, maxLife) # If you need a non dynamic lifetime, just make these both the same
        self.decays = decays # Set this to false to make the particles never delay (good for one use systems)

        # Image and drawing variables
        self.color = color # Color fo the particle
        self.image = pygame.Surface([self.width, self.height]) # Default surface for particle
        self.image.fill(self.color) # Fill the image with the color
        self.rect = self.pos # Set the rect (top-left) to the position

    def draw(self, surface):
        """Draw the particle
        
        Keyword arguments:
        surface (pygame.Surface) : The surface to draw the particle on, usually passed from the projectile
        """
        
        # Facade drawings
        if self.activeFacade: # If we use a facade
            if self.facadeType == "square": # If its square
                pygame.draw.rect(surface, self.facadeColor, (self.pos.x, self.pos.y, self.facadeWidth, self.facadeHeight), 0) # Draw a square facade with the defined settings
            elif self.facadeType == "circle": # If its a circle
                pygame.draw.circle(surface, self.facadeColor, (self.pos.x, self.pos.y), self.facadeRadius, 0) # Draw a circular facade with the defined settings
            else: # If something was mistyped or a non-correct type was applied
                pass # Dont do anything

    def update(self):
        """Update the particle"""

        # Update the position
        self.pos += self.velocity * reference.dt # Add the velocity step * delta time
        self.rect = self.pos # Update the position of the rect to the pos (top-left)

        # Particle decay
        if self.decays: # If we decay
            self.lifetime -= 1 # Then lets decay!

            if self.lifetime <= 0: # If we have no more lifetime
                self.kill() # Then we are dead!

# Base class of the system, handles the sprite group and drawing the sprites
class ParticleSystem():
    def __init__(self, maxParticles=100):
        """Base container for particles, extended by each specific system
        
        Keyword arguments:
        maxParticles (int) : The maximum number of particles that the system is allowed to contain (default=100)
        """
        
        self.particles = pygame.sprite.Group() # Create a group to contain particles
        self.maxParticles = maxParticles # Set max particles

    def draw(self, surface):
        """Draw all the particles in the system
        
        Keyword arguments:
        surface (pygame.Surface) : The surface to draw the particles on, passed from projectile
        """
        
        self.particles.draw(surface) # Call the draw function of the particle class
        for p in self.particles: # For each particle
            p.draw(surface) # Update manually

# Extends the base particle system, (x, y) located the origin point of the particles
class FireParticleSystem(ParticleSystem):
    def __init__(self, x, y):
        """Particle system designed to look like fire spray
        
        Keyword arguments:
        x (int) : The horizontal position of the system
        y (int) : The vertical position of the system
        """
        
        super().__init__() # Initialize the super class ParticleSystem

        self.pos = pygame.math.Vector2(x, y) # Vector to contain the x and y position

        self.particleColor = reference.color.FIRE_PARTICLE # Set the particle color

        self.maxParticles = 50 # Set the maxParticle limit

        self.createParticles(self.maxParticles, 0, 25) # Create the maximum amount of particles with a lifetime of 0 - 25

    # Create an amount of particles and add them to the group to be updated and drawn
    def createParticles(self, count, minLife, maxLife):
        """Create particles for the system
        
        Keyword arguments:
        count (int) : The amount of particles to create
        minLife (int) : The minimum amount of updates the particles live
        maxLife (int) : The maximum amount of updates the particles live
        """
        
        for p in range(count): # Loop an amount of times equal to the count
            p = Particle(self.pos.x, self.pos.y, 5, 5, self.particleColor, minLife, maxLife) # Create the particle

            # Assign velocities as a floats
            p.velocity.x = random.uniform(-50, 50) # These numbers are bigger than before due to the delta time update
            p.velocity.y = random.uniform(-50, 50) # Same as above

            # Randomly assign an alpha value to some of the particles for dynamic contrast
            p.image.set_alpha(random.randint(25, 255)) # Add a random opacity to the particle (it looks good)
    
            self.particles.add(p) # Add the particles to the group

    # Only calls for the particles to update, and continues the animation if the particles are allowed to decay
    def update(self):
        """Update the particles"""

        self.particles.update() # Call the particles update function

        # Keeps the particle count correct
        newCount = self.maxParticles - len(self.particles) # Get the amount of particles that have died
        self.createParticles(newCount, 25, 75) # Recreate them

class MagicParticleSystem(ParticleSystem):
    def __init__(self, x, y):
        """Very close the the fire system, just smaller and purple!
        
        Keyword arguments:
        x (int) : The horizontal position of the system
        y (int) : The vertical position of the system
        """
        
        super().__init__() # Intialize the super class (particleSystem)

        self.pos = pygame.math.Vector2(x, y) # Contains the x and y pos

        self.particleColor = (255, 0, 255) # Set the particle color

        self.maxParticles = 20 # Set the maximum number of particles

        self.createParticles(self.maxParticles, 0, 25) # Create our maximum number of particles

    # Create an amount of particles and add them to the group to be updated and drawn
    def createParticles(self, count, minLife, maxLife):
        """Create particles for the system
        
        Keyword arguments:
        count (int) : The amount of particles to create
        minLife (int) : The minimum amount of updates the particles live
        maxLife (int) : The maximum amount of updates the particles live
        """

        for p in range(count): # Create particles equal to the count
            p = Particle(self.pos.x, self.pos.y, 2, 2, self.particleColor, minLife, maxLife) # Create the particle

            # Assign velocities as a float for more fluid movement
            p.velocity.x = random.uniform(-20, 20) # Smaller numbers here mean less spread over lifetime (tighter line)
            p.velocity.y = random.uniform(-20, 20) # See above

            # Randomly assign an alpha value to some of the particles for dynamic contrast
            p.image.set_alpha(random.randint(25, 255)) # Random opacity is fun
            
            self.particles.add(p) # Add the particles to the group

    # Only calls for the particles to update, and continues the animation if the particles are allowed to decay
    def update(self):
        """Update the particles"""

        self.particles.update() # Call the master update

        # Keeps the particle count correct
        newCount = self.maxParticles - len(self.particles) # Get the amount of dead particles
        self.createParticles(newCount, 25, 75) # Necromancy!

#
#
# Extends the base particle system, this one uses both partical override and a facade system allowing for circles!
class SmokePuffParticleSystem(ParticleSystem):
    def __init__(self, x, y, puffDirection, particleOverride):
        """Particle system designed to look like a smoke puff (musket smoke?)
        
        Keyword arguments:
        x (int) : The horizontal position of the system
        y (int) : The vertical position of the system
        puffDirection (string) : The direction of the puff (currently only left or right)
        particleOverride (?) : I forget what this does?
        """
        
        super().__init__(particleOverride) # Initialize the particle system (I forget what the particleOverride is for?)

        self.pos = pygame.math.Vector2(x, y) # We have our trusty x, y vector

        self.puffDirection = puffDirection # The direction that we are firing the puff out in

        self.particleColor = (175, 175, 175) # The color of the particles

        self.createParticles(self.maxParticles) # Create the max amount of particles

    def createParticles(self, count):
        """Create particles for the system
        
        Keyword arguments:
        count (int) : The amount of particles to create
        """
        for p in range(count): # Create a number of particles equal to the count
            p = Particle(self.pos.x, self.pos.y, 1, 1, self.particleColor, 40, 50) # Adding a particle color here is not necessary as we set it to alpha, but this is as good as it gets currently without two particle classes
            p.activeFacade = True # Enable the facade in the particle system
            p.facadeType = "circle" # Set the facade type to a circle
            p.facadeRadius = 3 # Initial "puff" radius

            puffColor = random.randint(200, 255) # Create a random value (within a range that can be used for the r, g, b colors)

            p.facadeColor = (puffColor, puffColor, puffColor) # Use that same value to get uniform gray (this is different for every particle)

            # Determine the driection the particle needs to move, same as before
            if self.puffDirection == "left": # If that direction is left
                p.velocity.x = random.uniform(-1.0, -5.0) # We only get negative values
            elif self.puffDirection == "right": # Otherwise if its right
                p.velocity.x = random.uniform(1.0, 5.0) # We only get positive values

            # Because it is smoke, this can be a positive or negative value so that the smoke puff fluffs out as you would expect
            p.velocity.y = random.uniform(-0.5, 0.5) # The smoke currently only drifs upwards... But this isnt very useful after the perspective shift

            p.image.set_alpha(0) # This kills the opacity of the initial particle, allowing only the facade to be shown

            self.particles.add(p) # Add the particle to the particle group

    def update(self):
        """Update the particle system"""

        self.particles.update() # Update the particles

        for p in self.particles: # For each particle
            p.facadeRadius += random.uniform(0.1, 1.0) # Increase the radius by a non standard value (smoke puffs get bigger)

            # Reduce the velocity of the puff to a number nearing 0, without ever inverting the velocity of the puff. Most puffs will die before we get here
            if p.velocity.x >= 0.1: # If our velocity is positive (moving right)
                p.velocity.x -= 0.1 # Reduce it (cancell it left)
            if p.velocity.x <= -0.1: # If our velocity is negative (moving left)
                p.velocity.x += 0.1 # Increase it (cancell with right)

class PlayerParticleSystem(ParticleSystem):
    def __init__(self, x, y):
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)

        self.particleColor = reference.color.getRandomChoice([reference.color.PLAYER_PARTICLE_1, reference.color.PLAYER_PARTICLE_2, reference.color.PLAYER_PARTICLE_3])

        self.maxParticles = 300

        self.createParticles(self.maxParticles, 10, 25)

    # Create an amount of particles and add them to the group to be updated and drawn
    def createParticles(self, count, minLife, maxLife):
        """Create particles for the system
        
        Keyword arguments:
        count (int) : The amount of particles to create
        minLife (int) : The minimum amount of updates the particles live
        maxLife (int) : The maximum amount of updates the particles live
        """

        for p in range(count): # Create particles equal to the count
            particleDim = random.randint(3, 5)
            spawnOffset = 15
            spawnPos = pygame.math.Vector2(random.randint(int(self.pos.x) - spawnOffset, int(self.pos.x) + spawnOffset), random.randint(int(self.pos.y) - spawnOffset, int(self.pos.y) + spawnOffset))
            self.particleColor = reference.color.getRandomChoice([reference.color.PLAYER_PARTICLE_1, reference.color.PLAYER_PARTICLE_2, reference.color.PLAYER_PARTICLE_3])
            p = Particle(spawnPos.x, spawnPos.y, particleDim, particleDim, self.particleColor, minLife, maxLife) # Create the particle

            # Assign velocities as a float for more fluid movement
            p.velocity.x = random.uniform(-40, 40) # Smaller numbers here mean less spread over lifetime (tighter line)
            p.velocity.y = random.uniform(-40, 40) # See above

            # Randomly assign an alpha value to some of the particles for dynamic contrast
            p.image.set_alpha(random.randint(25, 255)) # Random opacity is fun
            
            self.particles.add(p) # Add the particles to the group

    # Only calls for the particles to update, and continues the animation if the particles are allowed to decay
    def update(self):
        """Update the particles"""

        self.particles.update() # Call the master update

        # Keeps the particle count correct
        newCount = self.maxParticles - len(self.particles) # Get the amount of dead particles
        self.createParticles(newCount, 10, 25) # Necromancy!

class ContainedParticle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, minLife, maxLife):
        """Contained particle for contained particle system
        
        Keyword arguments:
        x (int) : The horizontal position of the particle
        y (int) : The veritcal position of the particle
        width (int) : The width of the particle
        height (int) : The height of the particle
        color (pygame.Color) : The color of the particle system
        minLife (int) : The minimum amount of particle updates that the particle lives for
        maxLife (int) : The maximum amount of particle updates that the particle lives for
        """

        self.pos = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2()

        self.width = width
        self.height = height

        self.lifetime = random.randint(minLife, maxLife)

        self.color = color
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_color(self.color)
        self.rect = self.pos

    def update(self):
        self.pos += self.velocity * reference.dt
        self.rect = self.pos

        self.lifetime -= 1

        if self.lifetime <= 0:
            self.kill()

class ContainedParticleSystem(pygame.sprite.Sprite):
    def __init__(self, maxParticles = 100):
        pygame.sprite.Sprite.__init__(self)
        """Base container for contained particles, extended by each specific system
        
        Keyword arguments:
        maxParticles (int) : The maximum number of particles that the system is allowed to contain (default=100)
        """
        
        self.displaySurface = None

        self.particles = pygame.sprite.Group() # Create a group to contain particles
        self.maxParticles = maxParticles # Set max particles

    def draw(self, surface):
        """Draw all the particles in the system"""
        
        print("Drawing!")

        self.particles.draw(surface) # Call the draw function of the particle class
        for p in self.particles: # For each particle
            p.draw(surface) # Update manually

class ExplosionContainedParticleSystem(ContainedParticleSystem):
    def __init__(self, x, y):
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)

        self.particleColor = reference.color.WHITE

        self.maxParticles = 150

        self.createParticles(self.maxParticles, 30, 45)

        self.image = pygame.Surface([1, 1])
        self.image.fill((self.particleColor))
        self.rect = self.image.get_rect()

        print("I exist!")

    # Create an amount of particles and add them to the group to be updated and drawn
    def createParticles(self, count, minLife, maxLife):
        """Create particles for the system
        
        Keyword arguments:
        count (int) : The amount of particles to create
        minLife (int) : The minimum amount of updates the particles live
        maxLife (int) : The maximum amount of updates the particles live
        """

        for p in range(count): # Create particles equal to the count
            p = Particle(self.pos.x, self.pos.y, 3, 3, self.particleColor, minLife, maxLife) # Create the particle

            # Assign velocities as a float for more fluid movement
            p.velocity.x = random.uniform(-40, 40) # Smaller numbers here mean less spread over lifetime (tighter line)
            p.velocity.y = random.uniform(-40, 40) # See above

            # Randomly assign an alpha value to some of the particles for dynamic contrast
            p.image.set_alpha(random.randint(25, 255)) # Random opacity is fun
            
            self.particles.add(p) # Add the particles to the group
        
    def update(self):
        self.particles.update()

        if len(self.particles) <= 0:
            self.kill()