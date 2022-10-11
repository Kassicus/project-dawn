# Standard library imports
import pygame
import random

# Particle class, extends sprite. Uses sprite drawing method (image/surface based)
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, min_life, max_life, decays=True):
        pygame.sprite.Sprite.__init__(self) # Init pygame sprite class

        # Position Vars
        self.x = x
        self.y = y
        self.x_vel = 0
        self.y_vel = 0

        # Dimension Vars
        self.width = width
        self.height = height
        
        self.color = color

        self.lifetime = random.randint(min_life, max_life) # If you need a non dynamic lifetime, just make these both the same
        self.decays = decays # Set this to false to make the particles never delay (good for one use systems)

        self.image = pygame.Surface([self.width, self.height]) # This is how a pygame sprite gets its base image
        self.image.fill(self.color) # This is how you fill that image

        self.rect = (self.x, self.y) # Similar to self.pos vars in other classes. pygame.sprite requires this to be called self.rect

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

# Base class of the system, handles the sprite group and drawing the sprites
class ParticleSystem():
    def __init__(self, max_particles=250):
        self.particles = pygame.sprite.Group()
        self.max_particles = max_particles

    def draw(self, surface):
        self.particles.draw(surface)

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


class ImpactParticleSystem(ParticleSystem):
    def __init__(self, x, y, impact_direction, floor_offset, max_override):
        super().__init__(max_particles=max_override)
        self.x = x
        self.y = y

        self.origin_y = y

        self.impact_direction = impact_direction

        self.floor_offset = floor_offset

        self.particle_color = (50, 50, 50)

        self.createParticles(self.max_particles)

    def createParticles(self, count):
        for p in range(count):
            p = Particle(self.x, self.y, random.randint(3, 10), random.randint(3, 10), self.particle_color, 1000, 1500)

            if self.impact_direction == "left":
                p.x_vel = random.uniform(-0.5, -3.5)
            elif self.impact_direction == "right":
                p.x_vel = random.uniform(0.5, 3.5)

            p.y_vel = random.uniform(-3.5, 0.0)

            self.particles.add(p)

    def update(self):
        self.particles.update()

        for p in self.particles:
            p.y_vel += 0.075

            if p.y > self.origin_y + self.floor_offset:
                p.y_vel = 0
                p.x_vel = 0
                p.y = self.origin_y + self.floor_offset
