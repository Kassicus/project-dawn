# Standard library imports
import os
import string
import pygame
import pygame.color
import pygame.freetype as freetype

import lib
import menuBtn as btn

class BaseMenuScreen(): # Base menu screen for other types of menus to inherit (EX: Store Menu, Pause Menu, etc.)
    def __init__(self, x: int, y:int) -> None:
        """
        x: X value of menu origin coordinate
        y: Y value of menu origin coordinate
        
        """
        # Positioning Variables
        self.x = x
        self.y = y
        self.width = lib.SCREEN_WIDTH
        self.height = lib.SCREEN_HEIGHT

        # Color Variables
        self.colorPicker = pygame.color.Color
        self.fg_color = (0, 150, 0)
        self.bg_color = self.colorPicker("gray35")
        self.bg_color.a = 235
        self.textColor1 = "red2"
        self.textColor2 = "red3"
        self.textColor3 = "red4"
        self.gray22 = self.colorPicker("gray22")
        self.gray22.a = 225

        # Font Path Variables
        self.font = freetype.Font("data/Orbitron-Regular.ttf")  # type: ignore
        
        # Logic Variables
        self.isDrawn = False

        # Text Format Variables
        self.menuTitleTextSize = 64
        self.menuTextSize = 28
        self.screenNum = 1

        # Menu Format Variables
        self.menuRows = 5
        self.menuColumns = 3
        self.subScreenList :list[MenuSubScreen] = []
        
        # Surface Variables
        self.display_surface = pygame.display.get_surface()        
        self.menuScreenBackground = MenuSubScreen(self.x, self.y, self.width-(self.x*2), self.height-(self.y*2),self.bg_color)
        self.menuScreenBackground.surface.fill(self.bg_color)
        self.subScreenList.append(self.menuScreenBackground)

        # Background Surface Dimension Variables
        self.menuRowHeight = self.menuScreenBackground.surface.get_height()/self.menuRows #Variable for Row Height used in menu calculations
        self.menuColumnWidth = self.menuScreenBackground.surface.get_width()/self.menuColumns #Variable for Column Width used in menu calculations

class PauseMenu(BaseMenuScreen):
    def __init__(self, x: int, y:int) -> None:
        super().__init__(x,y)
        """
        x: X value of menu origin coordinate
        y: Y value of menu origin coordinate
        
        """
        # Dictionary Variables
        self.textCenterDict = {}   # Dictionary of Text Centered objects
        self.menuOptionDict = {}   # Dictionary of menuOptions
        
        # Dictionary Dynamic Key Name Base Definitions
        self.s1BtnKey = "menuSection1SubSection" # Base key name for a dynamic dictionary key. Dictionary:'menuSection1SubSections'. USE: Specifically to reference surface objects that are sub sections of menuSection1. EX: self.menuS1SSKeyname+str(1) = menuSection1SubSection1.
        self.textCenterS1Btn = "menuSec1BtnTxtCenter" # Base key name for a dynamic dictionary key. Dictionary:'textCenterDict'. USE: Secifically to reference the objects that get a surface's dimensions and centers text within them. More Specifically for Section1's SubSections in this case. EX: self.textCenterS1SSC+str(1) = menuSection1SubSectionTextCenter1.
        self.textCenterS2SSC = "menuSection2SubSectionTextCenter" # Base key name for a dynamic dictionary key. Dictionary:'textCenterDict'. USE: Secifically to reference the objects that get a surface's dimensions and centers text within them. More Specifically for Section2's SubSections in this case. EX: self.textCenterS1SSC+str(1) = menuSection1SubSectionTextCenter1.
        self.textCenterS3SSC = "menuSection3SubSectionTextCenter" # Base key name for a dynamic dictionary key. Dictionary:'textCenterDict'. USE: Secifically to reference the objects that get a surface's dimensions and centers text within them. More Specifically for Section3's SubSections in this case. EX: self.textCenterS1SSC+str(1) = menuSection1SubSectionTextCenter1.
        self.mO = "menuOption" # Base key name for a dynamic dictionary key. Dictionary:'menuOptionDict'. USE: Secifically to reference the text of the menu options. EX: self.mO+str(1) = menuOption1.

        
        # Text Variables
        self.menuTitle = "Character Management"
        self.fillerTxt = "Filler Text"
        s1BtnTextList = ["Character Info","Inventory","Astral Stash","Spell Book","Settings"]
        
        # Pause Menu Section Variables (Surfaces)
        self.menuTitleSection = MenuSubScreen(self.x,self.y,self.menuScreenBackground.width,self.menuRowHeight)
        self.menuSection1 = MenuSubScreen(self.x,(self.y+self.menuRowHeight),self.menuColumnWidth,self.menuRowHeight*2)
        #self.menuSection1.surface.fill(self.bg_color)
        self.menuSection2 = MenuSubScreen(self.x+self.menuColumnWidth,self.y+self.menuRowHeight,self.menuColumnWidth*2,self.menuRowHeight*2) 
        self.menuSection2.surface.fill(self.bg_color)
        self.menuSection3 = MenuSubScreen(self.x,self.y+self.menuRowHeight*3,self.menuScreenBackground.width,self.menuRowHeight*2) 
        self.menuSection3.surface.fill(self.bg_color)
        self.subScreenList.append(self.menuTitleSection)
        self.subScreenList.append(self.menuSection1)
        self.subScreenList.append(self.menuSection2)
        self.subScreenList.append(self.menuSection3)

        # Menu Section 1 Surface Dimension Variables
        self.menuSection1RowHeight = self.menuSection1.surface.get_height()/self.menuRows
        self.menuSection1ColumnWidth = self.menuSection1.surface.get_width()

        # Menu Section 1 Button Variables
        for s in range(1,self.menuRows+1):
            key = self.s1BtnKey+str(s)
            value = btn.Button(self.x,
                               self.y+self.menuRowHeight-self.menuSection1RowHeight+self.menuSection1RowHeight*s,
                               self.menuSection1ColumnWidth,
                               self.menuSection1RowHeight,
                               self.textColor2,
                               s1BtnTextList[s-1],
                               self.menuTextSize)
            if s == 2:
                value.isActive = True
                self.menuSection1.activeBtn = self.s1BtnKey+str(s)
                self.screenNum = s
            value.screenNum = s
            self.menuSection1.btnDict[key] = value

        # Text Centering Variables
        ## Menu Title Section
        self.menuTitleTextRect = self.font.get_rect(self.menuTitle, size = self.menuTitleTextSize)
        self.menuTitleTextRect.center = self.menuTitleSection.surface.get_rect().center

        ## Menu Section 2
        key = self.textCenterS2SSC
        value = self.font.get_rect(self.fillerTxt, size = self.menuTextSize)
        value.center = self.menuSection2.surface.get_rect().center
        self.textCenterDict[key] = value

        ## Menu Section 3
        key = self.textCenterS3SSC
        value = self.font.get_rect(self.fillerTxt, size = self.menuTextSize)
        value.center = self.menuSection3.surface.get_rect().center
        self.textCenterDict[key] = value
        

    def draw(self):
        
        
        # Rendering the separate menu elements 'together'. Background/Containers/Text

        ## Renders menu title text to the title section of the menu
        self.font.render_to(
        self.menuScreenBackground.surface,
        self.menuTitleTextRect,
        self.menuTitle,
        self.textColor1,
        size=self.menuTitleTextSize,
        style=freetype.STYLE_OBLIQUE,
        )
        self.font.pad = False

        ## Renders the button text to the buttons of section 1
        for i in range(1,self.menuRows+1):
            self.font.render_to(
            self.menuSection1.btnDict[self.s1BtnKey+str(i)].surface,
            self.menuSection1.btnDict[self.s1BtnKey+str(i)].btnTxtRect,
            self.menuSection1.btnDict[self.s1BtnKey+str(i)].btnTxt,
            self.menuSection1.btnDict[self.s1BtnKey+str(i)].btnTxtColor,
            size=self.menuTextSize,
            style=freetype.STYLE_UNDERLINE
            )
            self.font.pad = False

        ## Renders text to the center of section 2
        self.font.render_to(
        self.menuSection2.surface,
        self.textCenterDict[self.textCenterS2SSC],
        self.fillerTxt+" "+str(self.screenNum),
        self.textColor1,
        size=self.menuTextSize,
        style=freetype.STYLE_UNDERLINE 
        )
        self.font.pad = False

        ## Renders text to the center of section 3
        self.font.render_to(
        self.menuSection3.surface,
        self.textCenterDict[self.textCenterS3SSC],
        self.fillerTxt+" "+str(self.screenNum),
        self.textColor1,
        size=self.menuTextSize,
        style=freetype.STYLE_UNDERLINE 
        )
        self.font.pad = False

        # Blits various differant surfaces onto the Display Surface
        self.display_surface.blit(self.menuScreenBackground.surface,(self.x,self.y)) # Pause Menu Background
        self.display_surface.blit(self.menuSection1.surface,(self.menuSection1.x,self.menuSection1.y)) # Section 1 of Pause Menu
        for s in range(1,self.menuRows+1): # Section 1 Buttons
            self.display_surface.blit(self.menuSection1.btnDict[self.s1BtnKey+str(s)].surface,(self.x,(self.y+self.menuRowHeight-self.menuSection1RowHeight+self.menuSection1RowHeight*s)))
        self.display_surface.blit(self.menuSection2.surface,(self.menuSection2.x,self.menuSection2.y)) # Section 2 of Pause Menu
        self.display_surface.blit(self.menuSection3.surface,(self.menuSection3.x,self.menuSection3.y)) # Section 3 of Pause Menu
        
        # Draws border rects for surface bounds to make it look more clean
        pygame.draw.rect(self.display_surface, self.gray22, (self.menuSection1.x, self.menuSection1.y, self.menuSection1.width, self.menuSection1.height), 1) # MenuSection1Border
        pygame.draw.rect(self.display_surface, self.gray22, (self.menuSection2.x, self.menuSection2.y, self.menuSection2.width, self.menuSection2.height), 1) # MenuSection2Border
        pygame.draw.rect(self.display_surface, self.gray22, (self.menuSection3.x, self.menuSection3.y, self.menuSection3.width, self.menuSection3.height), 1) # MenuSection3Border
        pygame.draw.rect(self.display_surface, self.bg_color, (self.x, self.y, (self.width - (self.x * 2)), self.height - (self.y * 2)), 1) # MenuBorder

    def update(self):
        """Update the menu
        """
        mouse = pygame.mouse.get_pos()
        for i in range(1,len(self.menuSection1.btnDict.keys())+1):
            if self.menuSection1.btnDict[self.s1BtnKey+str(i)].x <= mouse[0] <= self.menuSection1.btnDict[self.s1BtnKey+str(i)].x+self.menuSection1.btnDict[self.s1BtnKey+str(i)].width and self.menuSection1.btnDict[self.s1BtnKey+str(i)].y <= mouse[1] <= self.menuSection1.btnDict[self.s1BtnKey+str(i)].y+self.menuSection1.btnDict[self.s1BtnKey+str(i)].height:
                    self.menuSection1.btnDict[self.s1BtnKey+str(i)].isHovered = True
            else: 
                self.menuSection1.btnDict[self.s1BtnKey+str(i)].isHovered = False
            if self.menuSection1.btnDict[self.s1BtnKey+str(i)].isHovered or self.menuSection1.btnDict[self.s1BtnKey+str(i)].isActive:
                self.menuSection1.btnDict[self.s1BtnKey+str(i)].btnTxtColor = self.textColor3
            else:
                self.menuSection1.btnDict[self.s1BtnKey+str(i)].btnTxtColor = self.textColor1
            self.menuSection1.btnDict[self.s1BtnKey+str(i)].surface = pygame.Surface((self.menuSection1.btnDict[self.s1BtnKey+str(i)].width,self.menuSection1.btnDict[self.s1BtnKey+str(i)].height),pygame.SRCALPHA)
        self.menuClick() 
        
        # Refresh all screens on menu to reduce build up
        refreshMenuScreens(self.subScreenList)       
    
    def menuClick(self):
        """Handles anything to do with clicking in the pause menu
        """
        
        if pygame.mouse.get_pressed()[0]: # Check for the mouse left click
            # mouseX, mouseY = pygame.mouse.get_pos() # Get the current mouse position
            for i in range(1,self.menuRows+1):
                if self.menuSection1.btnDict[self.s1BtnKey+str(i)].isHovered and self.menuSection1.btnDict[self.s1BtnKey+str(i)].isActive == False and self.menuSection1.activeBtn != self.s1BtnKey+str(i):
                    self.menuSection1.btnDict[self.menuSection1.activeBtn].isActive = False

                    self.menuSection1.activeBtn = self.s1BtnKey+str(i)
                    self.menuSection1.btnDict[self.s1BtnKey+str(i)].isActive = True
                    self.screenNum = self.menuSection1.btnDict[self.s1BtnKey+str(i)].screenNum                
                elif self.menuSection1.btnDict[self.s1BtnKey+str(i)].isHovered == False and self.menuSection1.activeBtn != self.s1BtnKey+str(i):
                    self.menuSection1.btnDict[self.s1BtnKey+str(i)].isActive = False
                
class MenuSubScreen():
    def __init__(self, x: int, y: int, width: float, height: float, bgColor: pygame.color.Color = None) -> None:
        """
        Arguments:
        x: X value of sub screen's origin coordinate
        y: Y value of sub screen's origin coordinate
        width: width of sub screen
        height: height of sub screen
        """
        self.surface = pygame.Surface((width,height),pygame.SRCALPHA)
        self.bgColor = bgColor
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.originPoint = (x,y)
        self.activeBtn = "" # Holds Dictionary key of current active button in the sub screen
        self.btnDict = {} # A dictionary of buttons on the sub screen

def refreshMenuScreens(subScreenList:list[MenuSubScreen]):
    for s in range(0,len(subScreenList)):
        subScreenList[s].surface = pygame.Surface((subScreenList[s].width, subScreenList[s].height), pygame.SRCALPHA)
        if subScreenList[s].bgColor is not None:
            subScreenList[s].surface.fill(subScreenList[s].bgColor)