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
        self.font = freetype.Font(os.path.join(fontdir, "data", "Orbitron-Regular.ttf"))  # type: ignore

        # Position Variables
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Graphics variables 
        self.colorPicker = pygame.color.Color
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.isDrawn = False

        # Font Variables
        self.menuTitle = "Character Management"
        self.menuOption1 = "Character Info"
        self.menuOption2 = "Inventory"
        self.menuOption3 = "Astral Stash"
        self.menuOption4 = "Spell Book"
        self.menuOption5 = "Settings"
        self.menuTitleTextSize = 64
        self.menuTextSize = 28

        # Font Color Variables
        self.textColor1 = "red3"

        # Surface Color Variables
        self.menuSection2Color = self.colorPicker("darkseagreen")
        self.menuSection2Color.a = 150
        self.menuSection3Color = self.colorPicker("darkslateblue")
        self.menuSection3Color.a = 150

        #Menu Format Variables
        self.menuRows = 5
        self.menuColumns = 3

        #Surface Variables
        self.menuScreenBackground = pygame.Surface((self.width - (self.x * 2), self.height - (self.y * 2)), pygame.SRCALPHA)
        self.menuScreenBackground.fill(self.bg_color)
        ##Background Surface Dimension Variables
        self.menuRowHeight = self.menuScreenBackground.get_height()/self.menuRows #Variable for Row Height used in menu calculations
        self.menuColumnWidth = self.menuScreenBackground.get_width()/self.menuColumns #Variable for Column Width used in menu calculations

        self.menuScreenTitleSection = pygame.Surface((self.menuScreenBackground.get_width(),self.menuRowHeight))
        self.menuMiddleRowSection = pygame.Surface((self.menuScreenBackground.get_width(),self.menuScreenBackground.get_height()))
        self.menuBottomRowSection = pygame.Surface((self.menuScreenBackground.get_width(),self.menuScreenBackground.get_height()*2-self.menuRowHeight))

        self.menuSection1 = pygame.Surface((self.menuColumnWidth,self.menuRowHeight*2),pygame.SRCALPHA)
        self.menuSection1.fill(self.bg_color)
        ##MenuSection1 Surface Dimension Variables
        self.menuSection1RowHeight = self.menuSection1.get_height()/self.menuRows
        self.menuSection1ColumnWidth = self.menuSection1.get_width()/self.menuColumns
        ###MenuSection1 Sub Surface Dimension Variables
        self.menuSection1SubSections = {}
        self.menuS1SSKeyName = "menuSectionSubSection" #menuSection1SubSectionKeyName: A dynamic variable essentially. Use in a dictionary key
        for s in range(1,self.menuRows+1):
            key = self.menuS1SSKeyName+str(s)
            value = pygame.Surface((self.menuSection1ColumnWidth*3,self.menuSection1RowHeight),pygame.SRCALPHA)
            #value.fill(self.bg_color)
            #dvalue.fill(self.menuSection2Color)
            self.menuSection1SubSections[key] = value

        self.menuSection2 = pygame.Surface((self.menuColumnWidth*2,self.menuRowHeight*2),pygame.SRCALPHA)
        self.menuSection2.fill(self.menuSection2Color)
        self.menuSection3 = pygame.Surface((self.menuColumnWidth*3,self.menuRowHeight*2),pygame.SRCALPHA)
        self.menuSection3.fill(self.menuSection3Color)

        #Text Centering Variables
        self.menuTitleTextRect = self.font.get_rect(self.menuTitle, size = self.menuTitleTextSize)
        self.menuTitleTextRect.center = self.menuScreenTitleSection.get_rect().center

        self.menuSection1Row1Center = self.font.get_rect(self.menuOption1, size = self.menuTextSize)
        self.menuSection1Row1Center.center = self.menuSection1SubSections[self.menuS1SSKeyName+str(1)].get_rect().center

        self.menuSection1Row2Center = self.font.get_rect(self.menuOption2, size = self.menuTextSize)
        self.menuSection1Row2Center.center = self.menuSection1SubSections[self.menuS1SSKeyName+str(2)].get_rect().center

        self.menuSection1Row3Center = self.font.get_rect(self.menuOption3, size = self.menuTextSize)
        self.menuSection1Row3Center.center = self.menuSection1SubSections[self.menuS1SSKeyName+str(3)].get_rect().center

        self.menuSection1Row4Center = self.font.get_rect(self.menuOption4, size = self.menuTextSize)
        self.menuSection1Row4Center.center = self.menuSection1SubSections[self.menuS1SSKeyName+str(4)].get_rect().center

        self.menuSection1Row5Center = self.font.get_rect(self.menuOption5, size = self.menuTextSize)
        self.menuSection1Row5Center.center = self.menuSection1SubSections[self.menuS1SSKeyName+str(5)].get_rect().center

        self.menuTitleTextRect2 = self.font.get_rect(self.menuTitle, size = self.menuTitleTextSize)
        self.menuTitleTextRect2.center = self.menuBottomRowSection.get_rect().center

    def draw(self, surface):
        # Rendering the separate menu elements 'together'. Background/Containers/Text
        ##region -Renders menu title to the top row section of the menu
        self.font.render_to(
        self.menuScreenBackground,
        self.menuTitleTextRect,
        self.menuTitle,
        self.textColor1,
        size=self.menuTitleTextSize,
        #style=freetype.STYLE_UNDERLINE #dd| freetype.STYLE_OBLIQUE,
        )
        self.font.pad = False
        ##endregion

        ##region -Renders menu title to the 2nd row section of the menu
        self.font.render_to(
        self.menuSection1SubSections[self.menuS1SSKeyName+str(1)],
        self.menuSection1Row1Center,
        self.menuOption1,
        self.textColor1,
        size=self.menuTextSize,
        style=freetype.STYLE_UNDERLINE #| freetype.STYLE_OBLIQUE,
        )
        self.font.pad = False
        ##endregion

        ##region -Renders menu title to the 2nd row section of the menu
        self.font.render_to(
        self.menuSection1SubSections[self.menuS1SSKeyName+str(2)],
        self.menuSection1Row2Center,
        self.menuOption2,
        self.textColor1,
        size=self.menuTextSize,
        style=freetype.STYLE_UNDERLINE #| freetype.STYLE_OBLIQUE,
        )
        self.font.pad = False
        ##endregion

        ##region -Renders menu title to the 2nd row section of the menu
        self.font.render_to(
        self.menuSection1SubSections[self.menuS1SSKeyName+str(3)],
        self.menuSection1Row3Center,
        self.menuOption3,
        self.textColor1,
        size=self.menuTextSize,
        style=freetype.STYLE_UNDERLINE #| freetype.STYLE_OBLIQUE,
        )
        self.font.pad = False
        ##endregion

        ##region -Renders menu title to the 2nd row section of the menu
        self.font.render_to(
        self.menuSection1SubSections[self.menuS1SSKeyName+str(4)],
        self.menuSection1Row4Center,
        self.menuOption4,
        self.textColor1,
        size=self.menuTextSize,
        style=freetype.STYLE_UNDERLINE #| freetype.STYLE_OBLIQUE,
        )
        self.font.pad = False
        ##endregion

        ##region -Renders menu title to the 2nd row section of the menu
        self.font.render_to(
        self.menuSection1SubSections[self.menuS1SSKeyName+str(5)],
        self.menuSection1Row5Center,
        self.menuOption5,
        self.textColor1,
        size=self.menuTextSize,
        style=freetype.STYLE_UNDERLINE #| freetype.STYLE_OBLIQUE,
        )
        self.font.pad = False
        ##endregion
        
        surface.blit(self.menuSection1,(self.x,(self.y+self.menuRowHeight)))
        for s in range(1,self.menuRows+1):
            surface.blit(self.menuSection1SubSections["menuSectionSubSection"+str(s)],(self.x,(self.y+self.menuRowHeight-self.menuSection1RowHeight+self.menuSection1RowHeight*s)))
        surface.blit(self.menuSection2,(self.x+self.menuColumnWidth,(self.y+self.menuRowHeight)))
        surface.blit(self.menuSection3,(self.x,(self.y+self.menuRowHeight*3)))
        surface.blit(self.menuScreenBackground,(self.x,self.y)) #MenuBackground
        #Region Menu wireframe guides
        # for i in range(1,self.menuRows+1):
        #     pygame.draw.line(self.menuSection1,self.fg_color,(0,self.menuSection1RowHeight*i),(self.menuSection1.get_width(),self.menuSection1RowHeight*i))
        # for i in range(1,self.menuColumns+1):
        #     pygame.draw.line(self.menuSection1,self.fg_color,(self.menuSection1ColumnWidth*i,self.menuSection1RowHeight),(self.menuSection1ColumnWidth*i,self.menuSection1.get_height()))
        #RegionEnd
        pygame.draw.rect(surface, self.bg_color, (self.x, self.y, (self.width - (self.x * 2)), self.height - (self.y * 2)), 1) # MenuBorder

    #def update(self, value):
    #    self.value = value # Update the value with a live feed
    #    self.current_value = int(self.width / self.max_value) * self.value # Refresh status bar width to match live value
