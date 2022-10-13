# Standard library imports
import os
import pygame
import pygame.color
import pygame.freetype as freetype

class PlayerInventoryMenu():
    def __init__(self, x, y, width, height, bg_color, fg_color):
        """
        bg_color: background color for menu
        fg_color: foreground color for menu
        
        """
        # Font Path Variables
        fontdir = os.path.dirname(os.path.abspath(__file__))
        self.font = freetype.Font(os.path.join(fontdir, "data", "Orbitron-Regular.ttf"))

        # Position Variables
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Graphics variables gray(69, 68, 65) dark-gray(41, 40, 37)
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.isDrawn = False

        self.menuTitle = "Inventory"
        self.menuTitleTextSize = 64
        self.menuRows = 5
        self.menuColumns = 3

        self.menuScreenBackground = pygame.Surface((self.width - (self.x * 2), self.height - (self.y * 2)), pygame.SRCALPHA)
        self.menuScreenBackground.fill(self.bg_color)

    def draw(self, surface):
        

        menuRowHeight = self.menuScreenBackground.get_height()/self.menuRows
        menuColumnWidth = self.menuScreenBackground.get_width()/self.menuColumns

        menuScreenTitleSection = pygame.Surface((self.menuScreenBackground.get_width(),menuRowHeight))
        menuMiddleRowSection = pygame.Surface((self.menuScreenBackground.get_width(),self.menuScreenBackground.get_height()))
        menuBottomRowSection = pygame.Surface((self.menuScreenBackground.get_width(),self.menuScreenBackground.get_height()*2-menuRowHeight))

        menuSection1 = pygame.Surface((menuColumnWidth,menuRowHeight*2),pygame.SRCALPHA)
        menuSection1.fill(self.bg_color)
        menuSection2 = pygame.Surface((menuColumnWidth*2,menuRowHeight*2),pygame.SRCALPHA)
        menuSection2.fill((69, 68, 65, 150))
        menuSection3 = pygame.Surface((menuColumnWidth*3,menuRowHeight*2),pygame.SRCALPHA)
        menuSection3.fill((179, 155, 86, 150))

        menuTitleTextRect = self.font.get_rect(self.menuTitle, size = self.menuTitleTextSize)
        menuTitleTextRect.center = menuScreenTitleSection.get_rect().center

        menuTitleTextRect1 = self.font.get_rect(self.menuTitle, size = self.menuTitleTextSize)
        menuTitleTextRect1.center = menuMiddleRowSection.get_rect().center

        menuTitleTextRect2 = self.font.get_rect(self.menuTitle, size = self.menuTitleTextSize)
        menuTitleTextRect2.center = menuBottomRowSection.get_rect().center

        # Rendering the separate menu elements 'together'. Background/Containers/Text

        ##region -Renders menu title to the top row section of the menu
        self.font.render_to(
        self.menuScreenBackground,
        menuTitleTextRect,
        self.menuTitle,
        "red3",
        #"dimgray",
        size=self.menuTitleTextSize,
        style=freetype.STYLE_UNDERLINE | freetype.STYLE_OBLIQUE,
        )
        self.font.pad = False
        ##endregion

        # ##region -Renders menu title to the 2nd row section of the menu
        # self.font.render_to(
        # self.menuScreenBackground,
        # menuTitleTextRect1,
        # self.menuTitle,
        # "red3",
        # #"dimgray",
        # size=self.menuTitleTextSize,
        # style=freetype.STYLE_UNDERLINE | freetype.STYLE_OBLIQUE,
        # )
        # self.font.pad = False
        # ##endregion

        # ##region -Renders menu title to the 2nd row section of the menu
        # self.font.render_to(
        # self.menuScreenBackground,
        # menuTitleTextRect2,
        # self.menuTitle,
        # "red3",
        # #"dimgray",
        # size=self.menuTitleTextSize,
        # style=freetype.STYLE_UNDERLINE | freetype.STYLE_OBLIQUE,
        # )
        # self.font.pad = False
        # ##endregion
        
        surface.blit(menuSection1,(self.x,(self.y+menuRowHeight)))
        surface.blit(menuSection2,(self.x+menuColumnWidth,(self.y+menuRowHeight)))
        surface.blit(menuSection3,(self.x,(self.y+menuRowHeight*3)))
        surface.blit(self.menuScreenBackground,(self.x,self.y)) #MenuBackground
        # #Region Menu wireframe guides
        # for i in range(1,self.menuRows+1):
        #     pygame.draw.line(self.menuScreenBackground,self.fg_color,(0,menuRowHeight*i),(self.menuScreenBackground.get_width(),menuRowHeight*i))
        # for i in range(1,self.menuColumns+1):
        #     pygame.draw.line(self.menuScreenBackground,self.fg_color,(menuColumnWidth*i,menuRowHeight),(menuColumnWidth*i,self.menuScreenBackground.get_height()))
        # #RegionEnd
        pygame.draw.rect(surface, self.bg_color, (self.x, self.y, (self.width - (self.x * 2)), self.height - (self.y * 2)), 1) # MenuBorder

    #def getTextLength():
    #def update(self, value):
    #    self.value = value # Update the value with a live feed
    #    self.current_value = int(self.width / self.max_value) * self.value # Refresh status bar width to match live value
