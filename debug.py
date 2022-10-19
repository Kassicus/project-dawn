# Standard library imports
import pygame
import projectile

class DebugInterface():
    def __init__(self):
        self.font = pygame.font.SysFont("Courier", 16)

        self.fps_text = None
        self.mouse_text = None
        self.player_text = None
        self.projectile_text = None
        self.particle_text = None

        self.display_surface = pygame.display.get_surface()

        self.active = False

        self.current_chunk_string = ""

    def get_fps(self, clock):
        fps_string = "FPS:     " + str(int(clock.get_fps()))
        fps_text = self.font.render(fps_string, 1, (255, 255, 255))
        return fps_text

    def get_mouse(self):
        mouse_string = "Mouse:  " + str(pygame.mouse.get_pos())
        mouse_text = self.font.render(mouse_string, 1, (255, 255, 255))
        return mouse_text

    def get_player(self, player):
        player_string = "Player: (" + str(player.rect.x) + ", " + str(player.rect.y) + ")"
        player_text = self.font.render(player_string, 1, (255, 255, 255))
        return player_text

    def get_projectile_count(self):
        projectile_string = "Proj:    " + str(int(len(projectile._projectiles)))
        projectile_text = self.font.render(projectile_string, 1, (255, 255, 255))
        return projectile_text

    def get_particle_count(self):
        particles = 0
        for p in projectile._projectiles:
            count = len(p.particle_system.particles)
            particles += count
        particle_string = "Part:    " + str(particles)
        particle_text = self.font.render(particle_string, 1, (255, 255, 255))
        return particle_text

    def draw(self):
        pygame.draw.rect(self.display_surface, (0, 0, 0), (780, 0, 220, 110), 0)
        self.display_surface.blit(self.fps_text, (800, 10))
        self.display_surface.blit(self.mouse_text, (800, 30))
        self.display_surface.blit(self.player_text, (800, 50))
        self.display_surface.blit(self.projectile_text, (800, 70))
        self.display_surface.blit(self.particle_text, (800, 90))

    def update(self, clock, player):
        self.fps_text = self.get_fps(clock)
        self.mouse_text = self.get_mouse()
        self.player_text = self.get_player(player)
        self.projectile_text = self.get_projectile_count()
        self.particle_text = self.get_particle_count()