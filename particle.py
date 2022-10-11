import pygame
import random

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, min_life, max_life, decays=True):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        self.x_vel = 0
        self.y_vel = 0

        self.width = width
        self.height = height
        
        self.color = color

        self.lifetime = random.randint(min_life, max_life)
        self.decays = decays

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        self.rect = (self.x, self.y)

    def update(self):

        self.x += self.x_vel
        self.y += self.y_vel

        self.rect = (self.x, self.y)

        if self.decays:
            self.lifetime -= 1

            if self.lifetime <= 0:
                self.kill()

class ParticleSystem():
    def __init__(self, max_particles=250):
        self.particles = pygame.sprite.Group()
        self.max_particles = max_particles

    def draw(self, surface):
        self.particles.draw(surface)

class FireParticleSystem(ParticleSystem):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

        self.particle_color = ((247, 90, 27))

    def createParticles(self, count):
        for p in range(count):
            p = Particle(self.x, self.y, 5, 5, self.particle_color, 25, 75)

            p.y_vel = random.uniform(-0.5, -3.5)
            p.x_vel = random.uniform(-0.5, 0.5)

            p.image.set_alpha(random.randint(25, 255))
                
            self.particles.add(p)

    def update(self):
        self.particles.update()

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
