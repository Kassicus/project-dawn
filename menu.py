# Standard library imports
import pygame
import pygame.color
import pygame.freetype as freetype

import lib
import menuBtn


displaySurface = lib.displaySurface
assetPath = "assets/.resources/"
assetDict = {}
assetDict["katana"] = assetPath+"katana.png"
assetDict["katanaLg"] = assetPath+"katanaLg.png"
assetDict["parchment"] = assetPath+"parchment.png"
assetDict["btnBorder"] = assetPath+"buttonBorder.png"
assetDict["sec2Half"] = assetPath+"sec2HalfBorder.png"

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
        self.menuLayout = MenuPage("pauseMenu")
        self.menuTitleSection = MenuSubScreen(self.x,self.y,self.menuScreenBackground.width,self.menuRowHeight,None,True)
        self.menuSection1 = MenuSubScreen(self.x,(self.y+self.menuRowHeight),self.menuColumnWidth,self.menuRowHeight*2,None,True)
        self.menuSection2 = MenuSubScreen(self.x+self.menuColumnWidth,self.y+self.menuRowHeight,self.menuColumnWidth*2,self.menuRowHeight*2,None,True)
        self.menuSection3 = MenuSubScreen(self.x,self.y+self.menuRowHeight*3,self.menuScreenBackground.width,self.menuRowHeight*2,None,True)
        self.menuLayout.addScreen(self.menuScreenBackground)
        self.menuLayout.addScreen(self.menuTitleSection)
        self.menuLayout.addScreen(self.menuSection1)
        self.menuLayout.addScreen(self.menuSection2)
        self.menuLayout.addScreen(self.menuSection3)

        # Inventory Sub Screen Variables
        self.inventoryLayout = MenuPage("inventory")
        itemDisplay = MenuSubScreen(self.menuSection2.x,self.menuSection2.y,self.menuSection2.width/2,self.menuSection2.height,None,False)
        itemDisplay.screenImgs.append(pygame.image.load(assetDict["sec2Half"]))
        itemDisplay.screenImgs.append(pygame.image.load(assetDict["katanaLg"]))
        itemInfo = MenuSubScreen(self.menuSection2.x+itemDisplay.width,self.menuSection2.y,self.menuSection2.width/2,self.menuSection2.height,self.colorPicker("black"),False)
        inventorySpace = MenuSubScreen(self.menuSection3.x,self.menuSection3.y,self.menuSection3.width,self.menuSection3.height,None,False,3,8)


        ## Inventory Space Buttons
        for s in range(1,inventorySpace.columns*inventorySpace.rows+1):
            if s <= 8:
                key = self.btnKey+str(s)
                value = menuBtn.Button(inventorySpace.x-inventorySpace.colWidth+inventorySpace.colWidth*s,
                                inventorySpace.y,
                                inventorySpace.colWidth,
                                inventorySpace.rowHeight,
                                self.textColor2,
                                "Button",
                                self.menuTextSize,
                                assetDict["btnBorder"],
                                assetDict["katana"])
                value.screenNum = s
                # value.surface.fill(self.gray22)
                inventorySpace.btnDict[key] = value
            elif 8<s<=16:
                key = self.btnKey+str(s)
                value = menuBtn.Button(inventorySpace.x-inventorySpace.colWidth+inventorySpace.colWidth*(s-8),
                                inventorySpace.y+inventorySpace.rowHeight,
                                inventorySpace.colWidth,
                                inventorySpace.rowHeight,
                                self.textColor2,
                                "Button",
                                self.menuTextSize,
                                assetDict["btnBorder"],
                                assetDict["katana"])
                value.screenNum = s
                #value.surface.fill(self.gray22)
                inventorySpace.btnDict[key] = value
            elif 16<s<=24:
                key = self.btnKey+str(s)
                value = menuBtn.Button(inventorySpace.x-inventorySpace.colWidth+inventorySpace.colWidth*(s-16),
                                inventorySpace.y+inventorySpace.rowHeight*2,
                                inventorySpace.colWidth,
                                inventorySpace.rowHeight,
                                self.textColor2,
                                "Button",
                                self.menuTextSize,
                                assetDict["btnBorder"],
                                assetDict["katana"])
                value.screenNum = s
                #value.surface.fill(self.gray22)
                inventorySpace.btnDict[key] = value

        self.inventoryLayout.addScreen(itemDisplay)
        self.inventoryLayout.addScreen(itemInfo)
        self.inventoryLayout.addScreen(inventorySpace)

        self.itemArt = self.font.get_rect("Item Art", size = self.menuTextSize)
        self.itemArt.center = self.inventoryLayout.screenList[0].surface.get_rect().center
        self.itemInfoText = self.font.get_rect("Item Info", size = self.menuTextSize)
        self.itemInfoText.center = self.inventoryLayout.screenList[1].surface.get_rect().center
        self.itemInventoryText = self.font.get_rect("Player Inventory", size = self.menuTextSize)
        self.itemInventoryText.center = self.inventoryLayout.screenList[2].surface.get_rect().center

        # Spell Book Sub Screen Variables
        self.spellBookLayout = MenuPage("spellBook")
        spellDisplay = MenuSubScreen(self.menuSection2.x,self.menuSection2.y,self.menuSection2.width/2,self.menuSection2.height,None,False)
        #spellDisplay.screenImgs.append(pygame.image.load('assets/.resources/sec2HalfBorder.png'))
        #spellDisplay.screenImgs.append(pygame.image.load('assets/.resources/katanaLg.png'))
        spellInfo = MenuSubScreen(self.menuSection2.x+itemDisplay.width,self.menuSection2.y,self.menuSection2.width/2,self.menuSection2.height,self.colorPicker("black"),False)
        spellBook = MenuSubScreen(self.menuSection3.x,self.menuSection3.y,self.menuSection3.width,self.menuSection3.height,None,False,8,3)

        # Spell Book Buttons
        for s in range(1,spellBook.columns*spellBook.rows+1):
            if s <= 8:
                key = self.btnKey+str(s)
                value = menuBtn.Button(spellBook.x-spellBook.colWidth+spellBook.colWidth*s,
                                spellBook.y,
                                spellBook.colWidth,
                                spellBook.rowHeight,
                                self.textColor2,
                                "Button",
                                self.menuTextSize)
                value.screenNum = s
                # value.surface.fill(self.gray22)
                spellBook.btnDict[key] = value
            elif 8<s<=16:
                key = self.btnKey+str(s)
                value = menuBtn.Button(spellBook.x-spellBook.colWidth+spellBook.colWidth*(s-8),
                                spellBook.y+spellBook.rowHeight,
                                spellBook.colWidth,
                                spellBook.rowHeight,
                                self.textColor2,
                                "Button",
                                self.menuTextSize)
                value.screenNum = s
                #value.surface.fill(self.gray22)
                spellBook.btnDict[key] = value
            elif 16<s<=24:
                key = self.btnKey+str(s)
                value = menuBtn.Button(spellBook.x-spellBook.colWidth+spellBook.colWidth*(s-16),
                                spellBook.y+spellBook.rowHeight*2,
                                spellBook.colWidth,
                                spellBook.rowHeight,
                                self.textColor2,
                                "Button",
                                self.menuTextSize)
                value.screenNum = s
                #value.surface.fill(self.gray22)
                spellBook.btnDict[key] = value

        self.spellBookLayout.addScreen(spellDisplay)
        self.spellBookLayout.addScreen(spellInfo)
        self.spellBookLayout.addScreen(spellBook)
        # Menu Section 1 Surface Dimension Variables
        self.menuSection1RowHeight = self.menuSection1.surface.get_height()/self.menuRows
        self.menuSection1ColumnWidth = self.menuSection1.surface.get_width()

        # Menu Section 1 Button Variables
        for s in range(1,self.menuRows+1):
            key = self.btnKey+str(s)
            value = menuBtn.Button(self.x,
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
        if self.inventoryLayout.isDrawn == False:
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
        if self.inventoryLayout.isDrawn == False :
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
        self.inventoryLayout.screenList[1].surface,
        self.itemInfoText,
        "Item Info",
        self.textColor1,
        size=self.menuTextSize,
        style=freetype.STYLE_UNDERLINE
        )
        self.font.pad = False

        # Blits various differant surfaces onto the Display Surface
        displaySurface.blit(self.menuScreenBackground.surface,(self.x,self.y)) # Pause Menu Background
        displaySurface.blit(self.menuSection1.surface,(self.menuSection1.x,self.menuSection1.y)) # Section 1 of Pause Menu
        for s in range(1,self.menuRows+1): # Section 1 Buttons
            displaySurface.blit(self.menuSection1.btnDict[self.btnKey+str(s)].surface,(self.x,(self.y+self.menuRowHeight-self.menuSection1RowHeight+self.menuSection1RowHeight*s)))
        displaySurface.blit(self.menuSection2.surface,(self.menuSection2.x,self.menuSection2.y)) # Section 2 of Pause Menu
        displaySurface.blit(self.menuSection3.surface,(self.menuSection3.x,self.menuSection3.y)) # Section 3 of Pause Menu
        for s in range(0,len(self.inventoryLayout.screenList)):
            screen = self.inventoryLayout.screenList[s]
            if screen.isDrawn:
                displaySurface.blit(screen.surface,screen.originPoint)
                if len(screen.screenImgs) > 0:
                    for i in range(0,len(screen.screenImgs)):
                        img = screen.screenImgs[i]
                        xCentered = screen.x+screen.width/2-img.get_width()/2
                        yCentered = screen.y+screen.height/2-img.get_height()/2
                        displaySurface.blit(screen.screenImgs[i],(xCentered,yCentered))
                self.inventoryLayout.screenList[2].blitButtons()
        
        for s in range(0,len(self.spellBookLayout.screenList)):
            screen = self.spellBookLayout.screenList[s]
            if screen.isDrawn:
                displaySurface.blit(screen.surface,screen.originPoint)
                if len(screen.screenImgs) > 0:
                    for i in range(0,len(screen.screenImgs)):
                        img = screen.screenImgs[i]
                        xCentered = screen.x+screen.width/2-img.get_width()/2
                        yCentered = screen.y+screen.height/2-img.get_height()/2
                        displaySurface.blit(screen.screenImgs[i],(xCentered,yCentered))
                if s == 2:
                    img = pygame.image.load(assetDict["parchment"])
                    displaySurface.blit(img,screen.originPoint)
                self.spellBookLayout.screenList[2].blitButtons()
                
        
                # for i in range(0,self.inventoryLayout.screenList[2].columns+1):
                #     section = self.inventoryLayout.screenList[2]
                #     pygame.draw.line(displaySurface,self.colorPicker("green"),(section.x+section.colWidth*i,section.y),(section.x+section.colWidth*i,section.y+section.height))
                # for i in range(0,self.inventoryLayout.screenList[2].rows+1):
                #     section = self.inventoryLayout.screenList[2]
                #     pygame.draw.line(displaySurface,self.colorPicker("green"),(section.x,section.y+section.rowHeight*i),(section.x+section.width,section.y+section.rowHeight*i))
        # Draws border rects for surface bounds to make it look more clean
        pygame.draw.rect(displaySurface, self.gray22, (self.menuSection1.x, self.menuSection1.y, self.menuSection1.width, self.menuSection1.height), 1) # MenuSection1Border
        pygame.draw.rect(displaySurface, self.gray22, (self.menuSection2.x, self.menuSection2.y, self.menuSection2.width, self.menuSection2.height), 1) # MenuSection2Border
        pygame.draw.rect(displaySurface, self.gray22, (self.menuSection3.x, self.menuSection3.y, self.menuSection3.width, self.menuSection3.height), 1) # MenuSection3Border
        pygame.draw.rect(displaySurface, self.bg_color, (self.x, self.y, (self.width - (self.x * 2)), self.height - (self.y * 2)), 1) # MenuBorder


    def update(self):
        """Update the menu
        """
        displaySurface = pygame.display.get_surface()
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
                    # elif self.menuSection1.btnDict[self.btnKey+str(i)].btnTxt == "Spell Book":
                    #     self.spellBookLayout.isDrawn = True
                    #     self.spellBookLayout.setIsDrawn()
                    else:
                        self.inventoryLayout.isDrawn = False
                        self.inventoryLayout.setIsDrawn()
                        # self.spellBookLayout.isDrawn = False
                        # self.spellBookLayout.setIsDrawn()
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
        self.parentPageName = ""
        self.btnKey = "btn"
        self.screenImgs:list[pygame.Surface] = []
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

    def blitButtons(self):
        for i in range(1,len(self.btnDict)+1):
            btn = self.btnDict[self.btnKey+str(i)]
            displaySurface.blit(btn.surface,(btn.x,btn.y))
            displaySurface.blit(btn.bkImg,btn.bkImgCent)
            displaySurface.blit(btn.img,btn.imgCent)
            # if self.parentPageName == "inventory":
            #     bkimg = pygame.image.load('assets/.resources/buttonBorder.png')
            #     x_centered = btn.x+btn.width / 2 - bkimg.get_width() / 2
            #     y_centered = btn.y+btn.height / 2 - bkimg.get_height() / 2 #similarly..
            #     displaySurface.blit(bkimg,(x_centered,y_centered))
            #     img = pygame.image.load('assets/.resources/katana.png')
            #     x_centered = btn.x+btn.width / 2 - img.get_width() / 2
            #     y_centered = btn.y+btn.height / 2 - img.get_height() / 2 #similarly..
            #     displaySurface.blit(img,(x_centered,y_centered))


class MenuPage():
    def __init__(self,pageName:str) -> None:
        """
        A collection of Sub Screens to be loaded EX: Inventory Page
        """
        self.pageName = pageName
        self.isDrawn = False
        self.screenList :list[MenuSubScreen] = []
    def addScreen(self,screen:MenuSubScreen):
        screen.parentPageName = self.pageName
        self.screenList.append(screen)
    def setIsDrawn(self):
        if self.isDrawn:
            for s in range(0,len(self.screenList)):
                self.screenList[s].isDrawn = True
        else:
            for s in range(0,len(self.screenList)):
                self.screenList[s].isDrawn = False
    # def drawScreens(self):
    #     for s in range(0,len(self.screenList)):
    #         screen = self.screenList[s]
    #         if screen.isDrawn:
    #             displaySurface.blit(screen.surface,screen.originPoint)
    #             if len(screen.screenImgs) > 0:
    #                 for i in range(0,len(screen.screenImgs)):
    #                     img = screen.screenImgs[i]
    #                     xCentered = screen.x+screen.width/2-img.get_width()/2
    #                     yCentered = screen.y+screen.height/2-img.get_height()/2
    #                     displaySurface.blit(screen.screenImgs[i],(xCentered,yCentered))
    #             self.inventoryLayout.screenList[2].blitButtons()

def refreshMenuScreens(subScreenList:list[MenuSubScreen]):
    for s in range(0,len(subScreenList)):
        subScreenList[s].surface = pygame.Surface((subScreenList[s].width, subScreenList[s].height), pygame.SRCALPHA)
        if subScreenList[s].bgColor is not None:
            subScreenList[s].surface.fill(subScreenList[s].bgColor)