# Standard library imports
import pygame
import pygame.examples.fonty
import pygame.examples.freetype_misc

# Custom class imports
import player
import ui
import projectile
import menu
import particle
import debug

pygame.init() # This only needs to be called once, at the top of the primary game file (main.py)

# Main game class (despite being a class this will only ever be instanciated once)
class Game():
    def __init__(self):
        # Window information variables
        self.screen_width = 1000
        self.screen_height = 800
        self.window_title = "Project Dawn"

        # Python screen setup
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        pygame.display.set_caption(self.window_title)

        # Game management variables
        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get() # Capturing this request into a variable to be used in other locations
        self.debuginterface = debug.DebugInterface()

        # Game object instances
        self.player = player.Player()

        self.healthbar = ui.StatusBar(10, 10, 200, 30, (87, 11, 6), (255, 0, 0), self.player.health, 100)

        # Testing the particle system
        self.fireEmitter = particle.FireParticleSystem(300, 400)
        self.fireEmitter.max_particles = 100
        
        self.puffEmitter = particle.SmokePuffParticleSystem(700, 400, "right", 20)

        self.impactEmitter = particle.ImpactParticleSystem(500, 200, "left", 200, 30)

        self.pMenu = menu.PlayerInventoryMenu(200, 100, self.screen_width, self.screen_height, (120,113,93,120), (0,150,0))

    # This function starts the game, but also starts the game loop, it determines the order of logic
    def start(self):
        while self.running:
            self.events = pygame.event.get()

            # Main event loop
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

                """
                TESTING
                [u]: decrease player health
                [i]: increase player health

                [m]: show menu

                [j]: emit smoke blast from player (only supports left and right currently)
                [k]: emit particle impact (static position currently)
                """
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        if self.player.health <= 90:
                            self.player.health += 10
                    if event.key == pygame.K_u:
                        if self.player.health >= 10:
                            self.player.health -= 10
                    if event.key == pygame.K_m:
                        if self.pMenu.isDrawn == False:
                            self.pMenu.isDrawn = True
                        else:
                            self.pMenu.isDrawn = False
                    if event.key == pygame.K_j:
                        self.puffEmitter.x = self.player.x
                        self.puffEmitter.y = self.player.y
                        self.puffEmitter.puff_direction = self.player.facing
                        self.puffEmitter.createParticles(self.puffEmitter.max_particles)
                    if event.key == pygame.K_k:
                        self.impactEmitter.createParticles(self.impactEmitter.max_particles)
                    if event.key == pygame.K_TAB:
                        if self.debuginterface.active:
                            self.debuginterface.active = False
                        else:
                            self.debuginterface.active = True
                """
                TESTING
                """

            self.draw()

            self.update()

    # Everything that needs to be drawn (graphical-updates) goes here
    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.debuginterface.active:
            self.debuginterface.draw(self.screen)
        # Draw all screen elements after this point

        self.player.draw(self.screen)
        self.healthbar.draw(self.screen)

        # This is a bit of a messy way to do this, sprites are shit, but its the easiest way to remove things from memory when you kill them
        # This will be refactored soon-ish
        for p in projectile._projectiles:
            p.draw(self.screen)

        self.fireEmitter.draw(self.screen)
        self.puffEmitter.draw(self.screen)
        self.impactEmitter.draw(self.screen)

        if self.pMenu.isDrawn == True:
            self.pMenu.draw(self.screen)

    # Everything that needs to be updated (non-graphical) goes here
    def update(self):
        self.player.update(self.events)
        self.healthbar.update(self.player.health)

        self.fireEmitter.update()
        self.puffEmitter.update()
        self.impactEmitter.update()

        # See above disclaimer for this...
        for p in projectile._projectiles:
            p.update()

        # Update all game elements before this point
        self.debuginterface.update(self.clock)
        pygame.display.update()
        self.clock.tick(30)

#testy = pygame.examples.fonty.main()
#testytype = pygame.examples.freetype_misc
#testytype.run()
game = Game() # Create an instance of the game class

game.start() # Start our instance of the game class

pygame.quit() # When the game.running variables is set back to false, the code resumes here and this line kills the game and all other pygame/python tasks on the machine created by the game