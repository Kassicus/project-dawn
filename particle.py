# Standard library imports
import pygame
import random

#
#
# Particle class, extends sprite. Uses sprite drawing method (image/surface based)
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, min_life, max_life, decays=True):
        pygame.sprite.Sprite.__init__(self) # Init pygame sprite class

        # Position Vars
        self.x = x
        self.y = y
        self.x_vel = 0
        self.y_vel = 0

        self.active_facade = False
        self.facade_type = ""
        self.facade_width = 0
        self.facade_height = 0
        self.facade_radius = 0

        self.facade_color = (0, 0, 0)

        # Dimension Vars
        self.width = width
        self.height = height
        
        self.color = color

        self.lifetime = random.randint(min_life, max_life) # If you need a non dynamic lifetime, just make these both the same
        self.decays = decays # Set this to false to make the particles never delay (good for one use systems)

        self.image = pygame.Surface([self.width, self.height]) # This is how a pygame sprite gets its base image
        self.image.fill(self.color) # This is how you fill that image

        self.rect = (self.x, self.y) # Similar to self.pos vars in other classes. pygame.sprite requires this to be called self.rect

    def draw(self, surface):
        if self.active_facade:
            if self.facade_type == "square":
                pygame.draw.rect(surface, self.facade_color, (self.x, self.y, self.facade_width, self.facade_height), 0)
            elif self.facade_type == "circle":
                pygame.draw.circle(surface, self.facade_color, (self.x, self.y), self.facade_radius, 0)
            else:
                pass

    # Handles all non-graphical updates for the particle
    def update(self):
        # Update the position
        self.x += self.x_vel
        self.y += self.y_vel
        self.rect = (self.x, self.y)

        # If the particle decays, reduce its life by 1 for each frame (~30/s)
        if self.decays:
            self.lifetime -= 1

            if self.lifetime <= 0:
                self.kill() # Fancy function to remove the particle from system memory (hacked in other classes, this is how its normally done)

#
#
# Base class of the system, handles the sprite group and drawing the sprites
class ParticleSystem():
    def __init__(self, max_particles=250):
        self.particles = pygame.sprite.Group()
        self.max_particles = max_particles

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
        self.x = x
        self.y = y

        self.particle_color = ((247, 90, 27))

    # Create an amount of particles and add them to the group to be updated and drawn
    def createParticles(self, count):
        for p in range(count):
            p = Particle(self.x, self.y, 5, 5, self.particle_color, 25, 75) # Create the particle (see particle class)

            # Assign velocities as a float for more fluid movement
            p.y_vel = random.uniform(-0.5, -3.5)
            p.x_vel = random.uniform(-0.5, 0.5)

            # Randomly assign an alpha value to some of the particles for dynamic contrast
            p.image.set_alpha(random.randint(25, 255))
            
            # Add the particles to the group
            self.particles.add(p)

    # Only calls for the particles to update, and continues the animation if the particles are allowed to decay
    def update(self):
        self.particles.update()

        # Keeps the particle count correct
        new_count = self.max_particles - len(self.particles)
        self.createParticles(new_count)

#
#
# Extends the base partical system, (x, y) located the origin point of the particles
class ImpactParticleSystem(ParticleSystem):
    def __init__(self, x, y, impact_direction, floor_offset, particle_override): # Particle override allows for the maximum particles on initail spawn of the system to be lower than 250
        super().__init__(particle_override) # Currently the only thing that can be passed in the super init
        self.x = x
        self.y = y

        self.origin_y = y # We need to track this so we can set a floor offset and have the particles stop at that "floor"

        self.impact_direction = impact_direction # If a bullet comes from the left, partices eject to the left (physics!)

        self.floor_offset = floor_offset # This is the pixel amount that we tell the particles they can fall before they hit a "floor"

        self.particle_color = (50, 50, 50)

        self.createParticles(self.max_particles)

    def createParticles(self, count):
        for p in range(count):
            p = Particle(self.x, self.y, random.randint(3, 10), random.randint(3, 10), self.particle_color, 100, 200)

            # Determine the direction the particle needs to be cast in and give it a random velocity (random float)
            if self.impact_direction == "left":
                p.x_vel = random.uniform(-0.5, -3.5)
            elif self.impact_direction == "right":
                p.x_vel = random.uniform(0.5, 10)

            p.y_vel = random.uniform(-3.5, 0.0) # Negative values send particles up, this is the initial velocity they are tossed up with

            self.particles.add(p)

    def update(self):
        self.particles.update()

        for p in self.particles:
            p.y_vel += 0.2 # Gravity!

            # Stop the particle if you hit the "floor"
            if p.y > self.origin_y + self.floor_offset:
                p.y_vel = 0
                p.x_vel = 0
                p.y = self.origin_y + self.floor_offset

#
#
# Extends the base particle system, this one uses both partical override and a facade system allowing for circles!
class SmokePuffParticleSystem(ParticleSystem):
    def __init__(self, x, y, puff_direction, particle_override):
        super().__init__(particle_override)
        self.x = x
        self.y = y

        self.puff_direction = puff_direction

        self.particle_color = (175, 175, 175)

        self.createParticles(self.max_particles)

    def createParticles(self, count):
        for p in range(count):
            p = Particle(self.x, self.y, 1, 1, self.particle_color, 40, 50) # Adding a particle color here is not necessary as we set it to alpha, but this is as good as it gets currently without two particle classes
            p.active_facade = True # Enable the facade in the particle system
            p.facade_type = "circle" # Set the facade type to a circle
            p.facade_radius = 3 # Initial "puff" radius

            puff_color = random.randint(100, 255) # Create a random value (within a range that can be used for the r, g, b colors)

            p.facade_color = (puff_color, puff_color, puff_color) # Use that same value to get uniform gray (this is different for every particle)

            # Determine the driection the particle needs to move, same as before
            if self.puff_direction == "left":
                p.x_vel = random.uniform(-1.0, -5.0)
            elif self.puff_direction == "right":
                p.x_vel = random.uniform(1.0, 5.0)

            # Because it is smoke, this can be a positive or negative value so that the smoke puff fluffs out as you would expect
            p.y_vel = random.uniform(-0.5, 0.5)

            p.image.set_alpha(0) # This kills the opacity of the initial particle, allowing only the facade to be shown

            self.particles.add(p)

    def update(self):
        self.particles.update()

        for p in self.particles:
            p.facade_radius += random.uniform(0.1, 1.0) # Increase the radius by a non standard value (smoke puffs get bigger)

            # Reduce the velocity of the puff to a number nearing 0, without ever inverting the velocity of the puff. Most puffs will die before we get here
            if p.x_vel >= 0.1:
                p.x_vel -= 0.1
            if p.x_vel <= -0.1:
                p.x_vel += 0.1