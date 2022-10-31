import pygame

import lib
import level

pygame.init()

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([lib.SCREEN_WIDTH, lib.SCREEN_HEIGHT])
        pygame.display.set_caption(lib.SCREEN_TITLE)

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.level = level.Level()

    def run(self):
        while self.running:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()
            self.update()

    def draw(self):
        self.screen.fill(lib.color.BLACK)
        self.level.draw()

    def update(self):
        self.level.update()
        pygame.display.update()
        lib.deltaTime = self.clock.tick() / 1000

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
