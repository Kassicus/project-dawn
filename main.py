import pygame

pygame.init()

class Game():
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 800
        self.window_title = "Project Dawn"

        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        pygame.display.set_caption(self.window_title)

        self.running = True

        self.clock = pygame.time.Clock()

    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill((0, 0, 0))

    def update(self):
        pygame.display.update()
        self.clock.tick(30)

game = Game()

game.start()

pygame.quit()