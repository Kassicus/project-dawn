# Standard library imports
import pygame
import random
import reference

#
#
# Particle class, extends sprite. Uses sprite drawing method (image/surface based)
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, minLife, maxLife, decays=True):
        pygame.sprite.Sprite.__init__(self) # Init pygame sprite class

        # Position Vars
        self.pos = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2()

        self.activeFacade = False
        self.facadeType = ""
        self.facadeWidth = 0
        self.facadeHeight = 0
        self.facadeRadius = 0

        self.facadeColor = (0, 0, 0)

        # Dimension Vars
        self.width = width
        self.height = height
        
        self.color = color

        self.lifetime = random.randint(minLife, maxLife) # If you need a non dynamic lifetime, just make these both the same
        self.decays = decays # Set this to false to make the particles never delay (good for one use systems)

        self.image = pygame.Surface([self.width, self.height]) # This is how a pygame sprite gets its base image
        self.image.fill(self.color) # This is how you fill that image

        self.rect = self.pos # Similar to self.pos vars in other classes. pygame.sprite requires this to be called self.rect

    def draw(self, surface):
        if self.activeFacade:
            if self.facadeType == "square":
                pygame.draw.rect(surface, self.facadeColor, (self.pos.x, self.pos.y, self.facadeWidth, self.facadeHeight), 0)
            elif self.facadeType == "circle":
                pygame.draw.circle(surface, self.facadeColor, (self.pos.x, self.pos.y), self.facadeRadius, 0)
            else:
                pass

    # Handles all non-graphical updates for the particle
    def update(self):
        # Update the position
        self.pos += self.velocity * reference.dt
        self.rect = self.pos

        # If the particle decays, reduce its life by 1 for each frame (~30/s)
        if self.decays:
            self.lifetime -= 1

            if self.lifetime <= 0:
                self.kill() # Fancy function to remove the particle from system memory (hacked in other classes, this is how its normally done)

#
#
# Base class of the system, handles the sprite group and drawing the sprites
class ParticleSystem():
    def __init__(self, maxParticles=100):
        self.particles = pygame.sprite.Group()
        self.maxParticles = maxParticles

    def draw(self, surface):
        self.particles.draw(surface)
        for p in self.particles:
            p.draw(surface)

#
#
# Extends the base particle system, (x, y) located the origin point of the particles
class FireParticleSystem(ParticleSystem):
    def __init__(self, x, y):
        super().__init__()
        self.pos = pygame.math.Vector2(x, y)

        self.particleColor = reference.COLOR_FIRE

        self.maxParticles = 50

        self.createParticles(self.maxParticles, 0, 25)

    # Create an amount of particles and add them to the group to be updated and drawn
    def createParticles(self, count, minLife, maxLife):
        for p in range(count):
            p = Particle(self.pos.x, self.pos.y, 5, 5, self.particleColor, minLife, maxLife) # Create the particle (see particle class)

            # Assign velocities as a float for more fluid movement
            p.velocity.x = random.uniform(-50, 50)
            p.velocity.y = random.uniform(-50, 50)

            # Randomly assign an alpha value to some of the particles for dynamic contrast
            p.image.set_alpha(random.randint(25, 255))
            
            # Add the particles to the group
            self.particles.add(p)

    # Only calls for the particles to update, and continues the animation if the particles are allowed to decay
    def update(self):
        self.particles.update()

        # Keeps the particle count correct
        newCount = self.maxParticles - len(self.particles)
        self.createParticles(newCount, 25, 75)

class MagicParticleSystem(ParticleSystem):
    def __init__(self, x, y):
        super().__init__()
        self.pos = pygame.math.Vector2(x, y)

        self.particleColor = (255, 0, 255)

        self.maxParticles = 20

        self.createParticles(self.maxParticles, 0, 25)

    # Create an amount of particles and add them to the group to be updated and drawn
    def createParticles(self, count, minLife, maxLife):
        for p in range(count):
            p = Particle(self.pos.x, self.pos.y, 2, 2, self.particleColor, minLife, maxLife) # Create the particle (see particle class)

            # Assign velocities as a float for more fluid movement
            p.velocity.x = random.uniform(-20, 20)
            p.velocity.y = random.uniform(-20, 20)

            # Randomly assign an alpha value to some of the particles for dynamic contrast
            p.image.set_alpha(random.randint(25, 255))
            
            # Add the particles to the group
            self.particles.add(p)

    # Only calls for the particles to update, and continues the animation if the particles are allowed to decay
    def update(self):
        self.particles.update()

        # Keeps the particle count correct
        newCount = self.maxParticles - len(self.particles)
        self.createParticles(newCount, 25, 75)

#
#
# Extends the base particle system, this one uses both partical override and a facade system allowing for circles!
class SmokePuffParticleSystem(ParticleSystem):
    def __init__(self, x, y, puffDirection, particleOverride):
        super().__init__(particleOverride)
        self.pos = pygame.math.Vector2(x, y)

        self.puffDirection = puffDirection

        self.particleColor = (175, 175, 175)

        self.createParticles(self.maxParticles)

    def createParticles(self, count):
        for p in range(count):
            p = Particle(self.pos.x, self.pos.y, 1, 1, self.particleColor, 40, 50) # Adding a particle color here is not necessary as we set it to alpha, but this is as good as it gets currently without two particle classes
            p.activeFacade = True # Enable the facade in the particle system
            p.facadeType = "circle" # Set the facade type to a circle
            p.facadeRadius = 3 # Initial "puff" radius

            puffColor = random.randint(200, 255) # Create a random value (within a range that can be used for the r, g, b colors)

            p.facadeColor = (puffColor, puffColor, puffColor) # Use that same value to get uniform gray (this is different for every particle)

            # Determine the driection the particle needs to move, same as before
            if self.puffDirection == "left":
                p.velocity.x = random.uniform(-1.0, -5.0)
            elif self.puffDirection == "right":
                p.velocity.x = random.uniform(1.0, 5.0)

            # Because it is smoke, this can be a positive or negative value so that the smoke puff fluffs out as you would expect
            p.velocity.y = random.uniform(-0.5, 0.5)

            p.image.set_alpha(0) # This kills the opacity of the initial particle, allowing only the facade to be shown

            self.particles.add(p)

    def update(self):
        self.particles.update()

        for p in self.particles:
            p.facadeRadius += random.uniform(0.1, 1.0) # Increase the radius by a non standard value (smoke puffs get bigger)

            # Reduce the velocity of the puff to a number nearing 0, without ever inverting the velocity of the puff. Most puffs will die before we get here
            if p.velocity.x >= 0.1:
                p.velocity.x -= 0.1
            if p.velocity.x <= -0.1:
                p.velocity.x += 0.1