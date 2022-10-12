# Standard library imports
import pygame

class DebugInterface():
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 16)

        self.fps_text = None
        self.mouse_text = None
        self.player_text = None
        self.current_chunk_text = None

        self.active = False

        self.current_chunk_string = ""

    def get_fps(self, clock):
        fps_string = "FPS:      " + str(int(clock.get_fps()))
        fps_text = self.font.render(fps_string, 1, (255, 255, 255))
        return fps_text

    def get_mouse(self):
        mouse_string = "Mouse:  " + str(pygame.mouse.get_pos())
        mouse_text = self.font.render(mouse_string, 1, (255, 255, 255))
        return mouse_text

    def get_player(self, player):
        player_string = "Player:   (" + str(player.rect.x) + ", " + str(player.rect.y) + ")"
        player_text = self.font.render(player_string, 1, (255, 255, 255))
        return player_text

    def get_current_chunk(self, room, player):
        get_chunk_id = room.containsPlayer(player)
        if get_chunk_id:
            self.current_chunk_string = "Chunk:   " + str(get_chunk_id)
        current_chunk_text = self.font.render(self.current_chunk_string, 1, (255, 255, 255))
        return current_chunk_text

    def draw(self, surface):
        surface.blit(self.fps_text, (850, 10))
        surface.blit(self.mouse_text, (850, 30))
        surface.blit(self.player_text, (850, 50))
        surface.blit(self.current_chunk_text, (850, 70))

    def update(self, clock, player, room):
        self.fps_text = self.get_fps(clock)
        self.mouse_text = self.get_mouse()
        self.player_text = self.get_player(player)
        self.current_chunk_text = self.get_current_chunk(room, player)