# Standard library imports
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
        self.menuScreenBackground = MenuSubScreen(self.x, self.y, self.width-(self.x*2), self.height-(self.y*2),self.bg_color,True)
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
        self.btnKey = "btn" # Base key name for a dynamic dictionary key. Dictionary:'MenuSubScreen().btnDict'. USE: Specifically to reference buttons that are sub sections of menuSection1. EX: self.s1BtnKey+str(1) = section1Btn1.
        self.textCenterS2SSC = "menuSection2SubSectionTextCenter" # Base key name for a dynamic dictionary key. Dictionary:'textCenterDict'. USE: Secifically to reference the objects that get a surface's dimensions and centers text within them. More Specifically for Section2's SubSections in this case. EX: self.textCenterS1SSC+str(1) = menuSection1SubSectionTextCenter1.
        self.textCenterS3SSC = "menuSection3SubSectionTextCenter" # Base key name for a dynamic dictionary key. Dictionary:'textCenterDict'. USE: Secifically to reference the objects that get a surface's dimensions and centers text within them. More Specifically for Section3's SubSections in this case. EX: self.textCenterS1SSC+str(1) = menuSection1SubSectionTextCenter1.


        # Text Variables
        self.menuTitle = "Character Management"
        self.fillerTxt = "Filler Text"
        s1BtnTextList = ["Character Info","Inventory","Astral Stash","Spell Book","Settings"]

        # Pause Menu Sub Screen Variables
        self.menuLayout = MenuPage()
        self.menuTitleSection = MenuSubScreen(self.x,self.y,self.menuScreenBackground.width,self.menuRowHeight,None,True)
        self.menuSection1 = MenuSubScreen(self.x,(self.y+self.menuRowHeight),self.menuColumnWidth,self.menuRowHeight*2,None,True)
        self.menuSection2 = MenuSubScreen(self.x+self.menuColumnWidth,self.y+self.menuRowHeight,self.menuColumnWidth*2,self.menuRowHeight*2,None,True)
        self.menuSection3 = MenuSubScreen(self.x,self.y+self.menuRowHeight*3,self.menuScreenBackground.width,self.menuRowHeight*2,None,True)
        self.menuLayout.screenList.append(self.menuScreenBackground)
        self.menuLayout.screenList.append(self.menuTitleSection)
        self.menuLayout.screenList.append(self.menuSection1)
        self.menuLayout.screenList.append(self.menuSection2)
        self.menuLayout.screenList.append(self.menuSection3)

        # Inventory Sub Screen Variables
        self.inventoryLayout = MenuPage()
        itemDisplay = MenuSubScreen(self.menuSection2.x,self.menuSection2.y,self.menuSection2.width/2,self.menuSection2.height,self.colorPicker("black"),False)
        itemInfo = MenuSubScreen(self.menuSection2.x+itemDisplay.width,self.menuSection2.y,self.menuSection2.width/2,self.menuSection2.height,self.colorPicker("white"),False)
        inventorySpace = MenuSubScreen(self.menuSection3.x,self.menuSection3.y,self.menuSection3.width,self.menuSection3.height,self.colorPicker("white"),False,3,8)


        ## Inventory Space Buttons
        for s in range(1,inventorySpace.columns*inventorySpace.rows+1):
            if s <= 8:
                key = self.btnKey+str(s)
                value = btn.Button(inventorySpace.x-inventorySpace.colWidth+inventorySpace.colWidth*s,
                                inventorySpace.y,
                                inventorySpace.colWidth,
                                inventorySpace.rowHeight,
                                self.textColor2,
                                "Button",
                                self.menuTextSize)
                value.screenNum = s
                #value.surface.fill(self.gray22)
                inventorySpace.btnDict[key] = value
            elif 8<s<=16:
                key = self.btnKey+str(s)
                value = btn.Button(inventorySpace.x-inventorySpace.colWidth+inventorySpace.colWidth*(s-8),
                                inventorySpace.y+inventorySpace.rowHeight,
                                inventorySpace.colWidth,
                                inventorySpace.rowHeight,
                                self.textColor2,
                                "Button",
                                self.menuTextSize)
                value.screenNum = s
                #value.surface.fill(self.gray22)
                inventorySpace.btnDict[key] = value
            elif 16<s<=24:
                key = self.btnKey+str(s)
                value = btn.Button(inventorySpace.x-inventorySpace.colWidth+inventorySpace.colWidth*(s-16),
                                inventorySpace.y+inventorySpace.rowHeight*2,
                                inventorySpace.colWidth,
                                inventorySpace.rowHeight,
                                self.textColor2,
                                "Button",
                                self.menuTextSize)
                value.screenNum = s
                #value.surface.fill(self.gray22)
                inventorySpace.btnDict[key] = value

        self.inventoryLayout.screenList.append(itemDisplay)
        self.inventoryLayout.screenList.append(itemInfo)
        self.inventoryLayout.screenList.append(inventorySpace)

        self.itemArt = self.font.get_rect("Item Art", size = self.menuTextSize)
        self.itemArt.center = self.inventoryLayout.screenList[0].surface.get_rect().center
        self.itemInfoText = self.font.get_rect("Item Info", size = self.menuTextSize)
        self.itemInfoText.center = self.inventoryLayout.screenList[1].surface.get_rect().center
        self.itemInventoryText = self.font.get_rect("Player Inventory", size = self.menuTextSize)
        self.itemInventoryText.center = self.inventoryLayout.screenList[2].surface.get_rect().center

        # Menu Section 1 Surface Dimension Variables
        self.menuSection1RowHeight = self.menuSection1.surface.get_height()/self.menuRows
        self.menuSection1ColumnWidth = self.menuSection1.surface.get_width()

        # Menu Section 1 Button Variables
        for s in range(1,self.menuRows+1):
            key = self.btnKey+str(s)
            value = btn.Button(self.x,
                               self.y+self.menuRowHeight-self.menuSection1RowHeight+self.menuSection1RowHeight*s,
                               self.menuSection1ColumnWidth,
                               self.menuSection1RowHeight,
                               self.textColor2,
                               s1BtnTextList[s-1],
                               self.menuTextSize)
            if s == 1:
                value.isActive = True
                self.menuSection1.activeBtn = self.btnKey+str(s)
                self.screenNum = s
                # self.inventoryLayout.isDrawn = True
                # self.inventoryLayout.setIsDrawn()
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
            self.menuSection1.btnDict[self.btnKey+str(i)].surface,
            self.menuSection1.btnDict[self.btnKey+str(i)].btnTxtRect,
            self.menuSection1.btnDict[self.btnKey+str(i)].btnTxt,
            self.menuSection1.btnDict[self.btnKey+str(i)].btnTxtColor,
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

        self.font.render_to(
        self.inventoryLayout.screenList[0].surface,
        self.itemArt,
        "Item Art",
        self.textColor1,
        size=self.menuTextSize,
        style=freetype.STYLE_UNDERLINE
        )
        self.font.pad = False

        self.font.render_to(
        self.inventoryLayout.screenList[1].surface,
        self.itemInfoText,
        "Item Info",
        self.textColor1,
        size=self.menuTextSize,
        style=freetype.STYLE_UNDERLINE
        )
        self.font.pad = False

        self.font.render_to(
        self.inventoryLayout.screenList[2].surface,
        self.itemInventoryText,
        "Player Inventory",
        self.textColor1,
        size=self.menuTextSize,
        style=freetype.STYLE_UNDERLINE
        )
        self.font.pad = False

        # Blits various differant surfaces onto the Display Surface
        self.display_surface.blit(self.menuScreenBackground.surface,(self.x,self.y)) # Pause Menu Background
        self.display_surface.blit(self.menuSection1.surface,(self.menuSection1.x,self.menuSection1.y)) # Section 1 of Pause Menu
        for s in range(1,self.menuRows+1): # Section 1 Buttons
            self.display_surface.blit(self.menuSection1.btnDict[self.btnKey+str(s)].surface,(self.x,(self.y+self.menuRowHeight-self.menuSection1RowHeight+self.menuSection1RowHeight*s)))
        self.display_surface.blit(self.menuSection2.surface,(self.menuSection2.x,self.menuSection2.y)) # Section 2 of Pause Menu
        self.display_surface.blit(self.menuSection3.surface,(self.menuSection3.x,self.menuSection3.y)) # Section 3 of Pause Menu
        for s in range(0,len(self.inventoryLayout.screenList)):
            if self.inventoryLayout.screenList[s].isDrawn:
                self.display_surface.blit(self.inventoryLayout.screenList[s].surface,self.inventoryLayout.screenList[s].originPoint)
                self.inventoryLayout.screenList[2].blitButtons(self.display_surface)

                value = self.inventoryLayout.screenList[2].btnDict["btn1"]
                bow = pygame.image.load('assets/.resources/bowArrow.png')
                self.display_surface.blit(bow,(value.x,value.y))
        
                for i in range(0,self.inventoryLayout.screenList[2].columns+1):
                    section = self.inventoryLayout.screenList[2]
                    pygame.draw.line(self.display_surface,self.colorPicker("green"),(section.x+section.colWidth*i,section.y),(section.x+section.colWidth*i,section.y+section.height))
                for i in range(0,self.inventoryLayout.screenList[2].rows+1):
                    section = self.inventoryLayout.screenList[2]
                    pygame.draw.line(self.display_surface,self.colorPicker("green"),(section.x,section.y+section.rowHeight*i),(section.x+section.width,section.y+section.rowHeight*i))
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
            if self.menuSection1.btnDict[self.btnKey+str(i)].x <= mouse[0] <= self.menuSection1.btnDict[self.btnKey+str(i)].x+self.menuSection1.btnDict[self.btnKey+str(i)].width and self.menuSection1.btnDict[self.btnKey+str(i)].y <= mouse[1] <= self.menuSection1.btnDict[self.btnKey+str(i)].y+self.menuSection1.btnDict[self.btnKey+str(i)].height:
                    self.menuSection1.btnDict[self.btnKey+str(i)].isHovered = True
            else:
                self.menuSection1.btnDict[self.btnKey+str(i)].isHovered = False
            if self.menuSection1.btnDict[self.btnKey+str(i)].isHovered or self.menuSection1.btnDict[self.btnKey+str(i)].isActive:
                self.menuSection1.btnDict[self.btnKey+str(i)].btnTxtColor = self.textColor3
            else:
                self.menuSection1.btnDict[self.btnKey+str(i)].btnTxtColor = self.textColor1
            self.menuSection1.btnDict[self.btnKey+str(i)].surface = pygame.Surface((self.menuSection1.btnDict[self.btnKey+str(i)].width,self.menuSection1.btnDict[self.btnKey+str(i)].height),pygame.SRCALPHA)
        self.menuClick()

        # Refresh all screens on menu to reduce build up
        refreshMenuScreens(self.menuLayout.screenList)
        refreshMenuScreens(self.inventoryLayout.screenList)

    def menuClick(self):
        """Handles anything to do with clicking in the pause menu
        """

        if pygame.mouse.get_pressed()[0]: # Check for the mouse left click
            # mouseX, mouseY = pygame.mouse.get_pos() # Get the current mouse position
            for i in range(1,self.menuRows+1):
                if self.menuSection1.btnDict[self.btnKey+str(i)].isHovered and self.menuSection1.btnDict[self.btnKey+str(i)].isActive == False and self.menuSection1.activeBtn != self.btnKey+str(i):
                    self.menuSection1.btnDict[self.menuSection1.activeBtn].isActive = False
                    self.menuSection1.activeBtn = self.btnKey+str(i)
                    self.menuSection1.btnDict[self.btnKey+str(i)].isActive = True
                    if self.menuSection1.btnDict[self.btnKey+str(i)].btnTxt == "Inventory":
                        self.inventoryLayout.isDrawn = True
                        self.inventoryLayout.setIsDrawn()
                    else:
                        self.inventoryLayout.isDrawn = False
                        self.inventoryLayout.setIsDrawn()
                    self.screenNum = self.menuSection1.btnDict[self.btnKey+str(i)].screenNum
                elif self.menuSection1.btnDict[self.btnKey+str(i)].isHovered == False and self.menuSection1.activeBtn != self.btnKey+str(i):
                    self.menuSection1.btnDict[self.btnKey+str(i)].isActive = False

class MenuSubScreen():
    def __init__(self, x: int, y: int, width: float, height: float, bgColor: pygame.color.Color = None,isDrawn:bool = False, rows:int = 1, columns:int = 1) -> None:
        """
        Arguments:
        x: X value of sub screen's origin coordinate
        y: Y value of sub screen's origin coordinate
        width: width of sub screen
        height: height of sub screen
        """
        self.btnKey = "btn"
        self.rows = rows
        self.rowHeight = height/rows
        self.columns = columns
        self.colWidth = width/columns
        self.isDrawn = isDrawn
        self.surface = pygame.Surface((width,height))
        self.bgColor = bgColor
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.originPoint = (x,y)
        self.activeBtn = "" # Holds Dictionary key of current active button in the sub screen
        self.btnDict = {} # A dictionary of buttons on the sub screen

    def blitButtons(self,surface):
        for i in range(1,len(self.btnDict)+1):
            button = self.btnDict[self.btnKey+str(i)]
            surface.blit(button.surface,(button.x,button.y))


class MenuPage():
    def __init__(self) -> None:
        """
        A collection of Sub Screens to be loaded EX: Inventory Page
        """
        self.isDrawn = False
        self.screenList :list[MenuSubScreen] = []
    def setIsDrawn(self):
        if self.isDrawn:
            for s in range(0,len(self.screenList)):
                self.screenList[s].isDrawn = True
        else:
            for s in range(0,len(self.screenList)):
                self.screenList[s].isDrawn = False

def refreshMenuScreens(subScreenList:list[MenuSubScreen]):
    for s in range(0,len(subScreenList)):
        subScreenList[s].surface = pygame.Surface((subScreenList[s].width, subScreenList[s].height), pygame.SRCALPHA)
        if subScreenList[s].bgColor is not None:
            subScreenList[s].surface.fill(subScreenList[s].bgColor)