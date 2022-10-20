# Standard library imports
import os
import pygame
import pygame.color
import pygame.freetype as freetype

import uni
import menuBtn as btn

class PlayerInventoryMenu():
    def __init__(self, x, y, bg_color, fg_color):
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
        self.width = uni.SCREEN_WIDTH
        self.height = uni.SCREEN_HEIGHT

        #Dictionary Variables
        self.menuS1BtnDict = {}         #menuSection1SubSections
        self.textCenterDict = {}   #Dictionary of Text Centered objects
        self.menuOptionDict = {}   #Dictionary of menuOptions
        
        #Dictionary Dynamic Key Name Base Definitions
        self.menuS1BtnKey = "menuSection1SubSection" #Base key name for a dynamic dictionary key. Dictionary:'menuSection1SubSections'. USE: Specifically to reference surface objects that are sub sections of menuSection1. EX: self.menuS1SSKeyname+str(1) = menuSection1SubSection1.
        self.textCenterS1SSC = "menuSection1SubSectionTextCenter" #Base key name for a dynamic dictionary key. Dictionary:'textCenterDict'. USE: Secifically to reference the objects that get a surface's dimensions and centers text within them. More Specifically for Section1's SubSections in this case. EX: self.textCenterS1SSC+str(1) = menuSection1SubSectionTextCenter1.
        self.textCenterS2SSC = "menuSection2SubSectionTextCenter" #Base key name for a dynamic dictionary key. Dictionary:'textCenterDict'. USE: Secifically to reference the objects that get a surface's dimensions and centers text within them. More Specifically for Section2's SubSections in this case. EX: self.textCenterS1SSC+str(1) = menuSection1SubSectionTextCenter1.
        self.textCenterS3SSC = "menuSection3SubSectionTextCenter" #Base key name for a dynamic dictionary key. Dictionary:'textCenterDict'. USE: Secifically to reference the objects that get a surface's dimensions and centers text within them. More Specifically for Section3's SubSections in this case. EX: self.textCenterS1SSC+str(1) = menuSection1SubSectionTextCenter1.
        
        self.mO = "menuOption" #Base key name for a dynamic dictionary key. Dictionary:'menuOptionDict'. USE: Secifically to reference the text of the menu options. EX: self.mO+str(1) = menuOption1.

        self.display_surface = pygame.display.get_surface()        

        # Graphics variables 
        self.colorPicker = pygame.color.Color
        # self.bg_color = bg_color
        self.bg_color = self.colorPicker("gray35")
        self.bg_color.a = 235
        self.fg_color = fg_color
        self.isDrawn = False

        # Font Variables
        self.menuTitle = "Character Management"
        self.menuOptionDict[self.mO] = "Filler Text"
        self.menuOptionDict[self.mO+str(1)] = "Character Info"
        self.menuOptionDict[self.mO+str(2)] = "Inventory"
        self.menuOptionDict[self.mO+str(3)] = "Astral Stash"
        self.menuOptionDict[self.mO+str(4)] = "Spell Book"
        self.menuOptionDict[self.mO+str(5)] = "Settings"
        self.menuTitleTextSize = 64
        self.menuTextSize = 28

        # Font Color Variables
        self.textColor1 = "red2"

        # Surface Color Variables
        self.menuSection2Color = self.colorPicker("gray22")
        self.menuSection2Color.a = 225
        self.menuSection3Color = self.colorPicker("gray23")
        self.menuSection3Color.a = 225

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
        #self.menuMiddleRowSection = pygame.Surface((self.menuScreenBackground.get_width(),self.menuScreenBackground.get_height()))
        #self.menuBottomRowSection = pygame.Surface((self.menuScreenBackground.get_width(),self.menuScreenBackground.get_height()*2-self.menuRowHeight))

        self.menuSection1 = pygame.Surface((self.menuColumnWidth,self.menuRowHeight*2),pygame.SRCALPHA)
        #self.menuSection1.fill(self.bg_color)
        ##MenuSection1 Surface Dimension Variables
        self.menuSection1RowHeight = self.menuSection1.get_height()/self.menuRows
        self.menuSection1ColumnWidth = self.menuSection1.get_width()/self.menuColumns
        ###MenuSection1 Sub Surface Dimension Variables
        for s in range(1,self.menuRows+1):
            key = self.menuS1BtnKey+str(s)
            value = btn.Button(self.x,
                               self.y+self.menuRowHeight-self.menuSection1RowHeight+self.menuSection1RowHeight*s,
                               self.menuSection1ColumnWidth*3,
                               self.menuSection1RowHeight,
                               "red3")
            #value = pygame.Surface((self.menuSection1ColumnWidth*3,self.menuSection1RowHeight),pygame.SRCALPHA)
            #value.fill(self.bg_color)
            #dvalue.fill(self.menuSection2Color)
            self.menuS1BtnDict[key] = value

        self.menuSection2 = pygame.Surface((self.menuColumnWidth*2,self.menuRowHeight*2),pygame.SRCALPHA)
        self.menuSection2.fill(self.bg_color)
        self.menuSection3 = pygame.Surface((self.menuColumnWidth*3,self.menuRowHeight*2),pygame.SRCALPHA)
        self.menuSection3.fill(self.bg_color)

        #Text Centering Variables
        ##Menu Title Section
        self.menuTitleTextRect = self.font.get_rect(self.menuTitle, size = self.menuTitleTextSize)
        self.menuTitleTextRect.center = self.menuScreenTitleSection.get_rect().center
        ##Menu Section 1
        for s in range(1,self.menuRows+1):
            key = self.textCenterS1SSC+str(s)
            value = self.font.get_rect(self.menuOptionDict[self.mO+str(s)] , size = self.menuTextSize)
            value.center = self.menuS1BtnDict[self.menuS1BtnKey+str(s)].surface.get_rect().center
            self.textCenterDict[key] = value
        ##Menu Section 2
        key = self.textCenterS2SSC
        value = self.font.get_rect(self.menuOptionDict[self.mO], size = self.menuTextSize)
        value.center = self.menuSection2.get_rect().center
        self.textCenterDict[key] = value
        ##Menu Section 3
        key = self.textCenterS3SSC
        value = self.font.get_rect(self.menuOptionDict[self.mO], size = self.menuTextSize)
        value.center = self.menuSection3.get_rect().center
        self.textCenterDict[key] = value
        

    def draw(self):
        mouse = pygame.mouse.get_pos()
        
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

        ##region -Renders the sub sections of section 1
        for i in range(1,self.menuRows+1):
            if self.menuS1BtnDict[self.menuS1BtnKey+str(i)].x <= mouse[0] <= self.menuS1BtnDict[self.menuS1BtnKey+str(i)].x+self.menuS1BtnDict[self.menuS1BtnKey+str(i)].width and self.menuS1BtnDict[self.menuS1BtnKey+str(i)].y <= mouse[1] <= self.menuS1BtnDict[self.menuS1BtnKey+str(i)].y+self.menuS1BtnDict[self.menuS1BtnKey+str(i)].height:
                self.menuS1BtnDict[self.menuS1BtnKey+str(i)].btnTxtColor = "red4"
            else: 
                self.menuS1BtnDict[self.menuS1BtnKey+str(i)].btnTxtColor = self.textColor1
            self.font.render_to(
            self.menuS1BtnDict[self.menuS1BtnKey+str(i)].surface,
            self.textCenterDict[self.textCenterS1SSC+str(i)],
            self.menuOptionDict[self.mO+str(i)],
            self.menuS1BtnDict[self.menuS1BtnKey+str(i)].btnTxtColor,
            size=self.menuTextSize,
            style=freetype.STYLE_UNDERLINE #| freetype.STYLE_OBLIQUE,
            )
            self.font.pad = False
        ##endregion
        ##region -Renders the sub sections of section 2
        #for i in range(1,self.menuRows+1):
        self.font.render_to(
        self.menuSection2,
        self.textCenterDict[self.textCenterS2SSC],
        self.menuOptionDict[self.mO],
        self.textColor1,
        size=self.menuTextSize,
        style=freetype.STYLE_UNDERLINE #| freetype.STYLE_OBLIQUE,
        )
        self.font.pad = False
        ##endregion
        ##region -Renders the sub sections of section 3
        #for i in range(1,self.menuRows+1):
        self.font.render_to(
        self.menuSection3,
        self.textCenterDict[self.textCenterS3SSC],
        self.menuOptionDict[self.mO],
        self.textColor1,
        size=self.menuTextSize,
        style=freetype.STYLE_UNDERLINE #| freetype.STYLE_OBLIQUE,
        )
        self.font.pad = False
        ##endregion

        self.display_surface.blit(self.menuScreenBackground,(self.x,self.y)) #MenuBackground
        self.display_surface.blit(self.menuSection1,(self.x,(self.y+self.menuRowHeight)))
        for s in range(1,self.menuRows+1):
            self.display_surface.blit(self.menuS1BtnDict[self.menuS1BtnKey+str(s)].surface,(self.x,(self.y+self.menuRowHeight-self.menuSection1RowHeight+self.menuSection1RowHeight*s)))
        self.display_surface.blit(self.menuSection2,(self.x+self.menuColumnWidth,(self.y+self.menuRowHeight)))
        self.display_surface.blit(self.menuSection3,(self.x,(self.y+self.menuRowHeight*3)))
        #Region Menu wireframe guides
        # for i in range(1,self.menuRows+1):
        #     pygame.draw.line(self.menuSection1,self.fg_color,(0,self.menuSection1RowHeight*i),(self.menuSection1.get_width(),self.menuSection1RowHeight*i))
        # for i in range(1,self.menuColumns+1):
        #     pygame.draw.line(self.menuSection1,self.fg_color,(self.menuSection1ColumnWidth*i,self.menuSection1RowHeight),(self.menuSection1ColumnWidth*i,self.menuSection1.get_height()))
        #RegionEnd
        pygame.draw.rect(self.display_surface, self.menuSection2Color, (self.x, self.y+self.menuRowHeight, self.menuColumnWidth, self.menuRowHeight*2), 1) # MenuSection1Border
        pygame.draw.rect(self.display_surface, self.menuSection2Color, (self.x+self.menuColumnWidth, self.y+self.menuRowHeight, self.menuColumnWidth*2, self.menuRowHeight*2), 1) # MenuSection2Border
        pygame.draw.rect(self.display_surface, self.menuSection2Color, (self.x, self.y+self.menuRowHeight*3, self.menuColumnWidth*3, self.menuRowHeight*2), 1) # MenuSection3Border
        pygame.draw.rect(self.display_surface, self.bg_color, (self.x, self.y, (self.width - (self.x * 2)), self.height - (self.y * 2)), 1) # MenuBorder

    def update(self, value):
       self.value = value # Update the value with a live feed
       self.current_value = int(self.width / self.max_value) * self.value # Refresh status bar width to match live value
