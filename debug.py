# Standard library imports
import pygame

class DebugInterface():
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 16)

        self.fps_text = None

        self.active = False

    def get_fps(self, clock):
        fps_string = "FPS: " + str(int(clock.get_fps()))
        fps_text = self.font.render(fps_string, 1, (255, 255, 255))
        return fps_text

    def draw(self, surface):
        surface.blit(self.fps_text, (900, 10))

    def update(self, clock):
        self.fps_text = self.get_fps(clock)