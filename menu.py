# Standard library imports
import pygame
import pygame.color
import pygame.freetype as freetype

# Custom library imports
import lib
import menuBtn

# Resource path variables
displaySurface = lib.displaySurface
assetPath = "assets/.resources/"
assetDict = {}
assetDict["katana"] = assetPath+"katana.png"
assetDict["katanaLg"] = assetPath+"katanaLg.png"
assetDict["parchment"] = assetPath+"parchment.png"
assetDict["btnBorder"] = assetPath+"buttonBorder.png"
assetDict["sec2Half"] = assetPath+"sec2HalfBorder.png"

# Color Variables
colorPicker = pygame.color.Color
fg_color = (0, 150, 0)
bg_color = colorPicker("gray35")
bg_color.a = 235
textColor1 = "red2"
textColor2 = "red3"
textColor3 = "red4"
gray22 = colorPicker("gray22")
gray22.a = 225

# Text Format Variables
menuTitleTextSize = 64
menuTextSize = 28
screenNum = 1

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

        # Font Path Variables
        self.font = freetype.Font("data/Orbitron-Regular.ttf")  # type: ignore

        # Logic Variables
        self.isDrawn = False

        # Menu Format Variables
        self.menuRows = 5
        self.menuColumns = 3
        self.subScreenList :list[MenuSubScreen] = []

        # Surface Variables
        self.menuScreenBackground = MenuSubScreen(self.x, self.y, self.width-(self.x*2), self.height-(self.y*2),bg_color,True)
        self.menuScreenBackground.surface.fill(bg_color)
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

        # Text Variables
        self.menuTitle = "Character Management"
        self.fillerTxt = "Filler Text"
        s1BtnTextList = ["Character Info","Inventory","Astral Stash","Spell Book","Settings"]

        # Pause Menu Sub Screen Variables
        self.menuLayout = MenuPage("pauseMenu")
        self.menuTitleSection = MenuSubScreen(self.x,self.y,self.menuScreenBackground.width,self.menuRowHeight,None,True)

        self.menuSection1 = MenuSubScreen(self.x,(self.y+self.menuRowHeight),self.menuColumnWidth,self.menuRowHeight*2,None,True,5)
        self.menuSection1.generateButtons(s1BtnTextList)
        self.menuSection1.btnDict[self.menuSection1.btnKey+str(1)].isActive = True
        self.menuSection1.activeBtn = self.menuSection1.btnKey+str(1)

        self.menuSection2 = MenuSubScreen(self.x+self.menuColumnWidth,self.y+self.menuRowHeight,self.menuColumnWidth*2,self.menuRowHeight*2,None,True)
        self.menuSection3 = MenuSubScreen(self.x,self.y+self.menuRowHeight*3,self.menuScreenBackground.width,self.menuRowHeight*2,None,True)
        self.menuLayout.addScreen(self.menuScreenBackground)
        self.menuLayout.addScreen(self.menuTitleSection)
        self.menuLayout.addScreen(self.menuSection1)
        self.menuLayout.addScreen(self.menuSection2)
        self.menuLayout.addScreen(self.menuSection3)

        # Inventory Sub Screen Variables
        self.inventoryLayout = MenuPage("inventory")
        itemDisplayImgs:list[pygame.Surface] = []
        itemDisplayImgs.append(pygame.image.load(assetDict["sec2Half"]))
        itemDisplayImgs.append(pygame.image.load(assetDict["katanaLg"]))
        itemDisplay = MenuSubScreen(self.menuSection2.x,self.menuSection2.y,self.menuSection2.width/2,self.menuSection2.height,None,False,screenImgs=itemDisplayImgs)
        itemInfo = MenuSubScreen(self.menuSection2.x+itemDisplay.width,self.menuSection2.y,self.menuSection2.width/2,self.menuSection2.height,colorPicker("black"),False)
        inventorySpace = MenuSubScreen(self.menuSection3.x,self.menuSection3.y,self.menuSection3.width,self.menuSection3.height,None,False,3,8)
        inventorySpace.generateButtons(bkImg=assetDict["btnBorder"],img=assetDict["katana"])

        self.inventoryLayout.addScreen(itemDisplay)
        self.inventoryLayout.addScreen(itemInfo)
        self.inventoryLayout.addScreen(inventorySpace)

        # Spell Book Sub Screen Variables
        self.spellBookLayout = MenuPage("spellBook")
        spellDisplay = MenuSubScreen(self.menuSection2.x,self.menuSection2.y,self.menuSection2.width/2,self.menuSection2.height,None,False)
        spellInfo = MenuSubScreen(self.menuSection2.x+spellDisplay.width,self.menuSection2.y,self.menuSection2.width/2,self.menuSection2.height,None,False)
        spellBook = MenuSubScreen(self.menuSection3.x,self.menuSection3.y,self.menuSection3.width,self.menuSection3.height,None,False,8,3,[pygame.image.load(assetDict["parchment"])])
        spellBook.generateButtons(btnTxt="Spell")
        
        self.spellBookLayout.addScreen(spellDisplay)
        self.spellBookLayout.addScreen(spellInfo)
        self.spellBookLayout.addScreen(spellBook)

        # Text Centering Variables
        self.menuTitleTextRect = self.font.get_rect(self.menuTitle, size = menuTitleTextSize)
        self.menuTitleTextRect.center = self.menuTitleSection.surface.get_rect().center

        self.itemInfoText = self.font.get_rect("Item Info", size = menuTextSize)
        self.itemInfoText.center = self.inventoryLayout.screenList[1].surface.get_rect().center

    def draw(self):
        # Rendering the separate menu elements 'together'. Background/Containers/Text
        ## Renders menu title text to the title section of the menu
        self.font.render_to(
        self.menuScreenBackground.surface,
        self.menuTitleTextRect,
        self.menuTitle,
        textColor1,
        size=menuTitleTextSize,
        style=freetype.STYLE_OBLIQUE,
        )
        self.font.pad = False

        self.font.render_to(
        self.inventoryLayout.screenList[1].surface,
        self.itemInfoText,
        "Item Info",
        textColor1,
        size=menuTextSize,
        style=freetype.STYLE_UNDERLINE
        )
        self.font.pad = False

        self.menuLayout.drawScreens()
        self.inventoryLayout.drawScreens()
        self.spellBookLayout.drawScreens()
        
        # Draws border rects for surface bounds to make it look more clean
        pygame.draw.rect(displaySurface, gray22, (self.menuSection1.x, self.menuSection1.y, self.menuSection1.width, self.menuSection1.height), 1) # MenuSection1Border
        pygame.draw.rect(displaySurface, gray22, (self.menuSection2.x, self.menuSection2.y, self.menuSection2.width, self.menuSection2.height), 1) # MenuSection2Border
        pygame.draw.rect(displaySurface, gray22, (self.menuSection3.x, self.menuSection3.y, self.menuSection3.width, self.menuSection3.height), 1) # MenuSection3Border
        pygame.draw.rect(displaySurface, bg_color, (self.x, self.y, (self.width - (self.x * 2)), self.height - (self.y * 2)), 1) # MenuBorder


    def update(self):
        """Update the menu
        """
        mouse = pygame.mouse.get_pos()
        for i in range(1,len(self.menuSection1.btnDict)+1):
            btn = self.menuSection1.btnDict[self.menuSection1.btnKey+str(i)]
            if btn.x <= mouse[0] <= btn.x+btn.width and btn.y <= mouse[1] <= btn.y+btn.height:
                    btn.isHovered = True
            else:
                btn.isHovered = False
            if btn.isHovered or btn.isActive:
                btn.btnTxtColor = textColor3
            else:
                btn.btnTxtColor = textColor1
            btn.surface = pygame.Surface((btn.width,btn.height),pygame.SRCALPHA)

        self.checkMenuClick()

        # Refresh all screens on menu to reduce build up
        refreshMenuScreens(self.menuLayout.screenList)
        refreshMenuScreens(self.inventoryLayout.screenList)
        refreshMenuScreens(self.spellBookLayout.screenList)

    def checkMenuClick(self):
        """Handles anything to do with clicking in the pause menu
        """
        if pygame.mouse.get_pressed()[0]: # Check for the mouse left click
            for i in range(1,self.menuSection1.rows+1):
                btn = self.menuSection1.btnDict[self.menuSection1.btnKey+str(i)]
                if btn.isHovered and btn.isActive == False and self.menuSection1.activeBtn != self.menuSection1.btnKey+str(i):
                    self.menuSection1.btnDict[self.menuSection1.activeBtn].isActive = False
                    self.menuSection1.activeBtn = self.menuSection1.btnKey+str(i)
                    btn.isActive = True
                    if btn.btnTxt == "Inventory":
                        self.inventoryLayout.isDrawn = True
                        self.inventoryLayout.setIsDrawn()
                        self.spellBookLayout.isDrawn = False
                        self.spellBookLayout.setIsDrawn()
                    elif btn.btnTxt == "Spell Book":
                        self.spellBookLayout.isDrawn = True
                        self.spellBookLayout.setIsDrawn()
                        self.inventoryLayout.isDrawn = False
                        self.inventoryLayout.setIsDrawn()
                    else:
                        self.inventoryLayout.isDrawn = False
                        self.inventoryLayout.setIsDrawn()
                        self.spellBookLayout.isDrawn = False
                        self.spellBookLayout.setIsDrawn()
                elif btn.isHovered == False and self.menuSection1.activeBtn != self.menuSection1.btnKey+str(i):
                    btn.isActive = False

class MenuSubScreen():
    def __init__(self, x: int, y: int, width: float, height: float, bgColor: pygame.color.Color = None,isDrawn:bool = False, rows:int = 1, columns:int = 1,screenImgs:list[pygame.Surface] = []) -> None:
        """
        Arguments:
        x: X value of sub screen's origin coordinate
        y: Y value of sub screen's origin coordinate
        width: width of sub screen
        height: height of sub screen
        """
        self.parentPageName = ""
        self.btnKey = "btn"
        self.screenImgs:list[pygame.Surface] = screenImgs
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

    def generateButtons(self,btnTxtList:list[str] = None, btnTxt:str=None,bkImg:str=None,img:str=None):
        ## Inventory Space Buttons
        c = 0
        r = 0
        for s in range(1,self.columns*self.rows+1):
            if btnTxtList is not None:
                btnTxt = btnTxtList[s-1]
            if c < self.columns-1:
                key = self.btnKey+str(s)
                value = menuBtn.Button(self.x+self.colWidth*c,
                                self.y+self.rowHeight*r,
                                self.colWidth,
                                self.rowHeight,
                                textColor2,
                                btnTxt,
                                menuTextSize,
                                bkImg,
                                img)
                value.screenNum = s
                c+=1
            else:
                key = self.btnKey+str(s)
                value = menuBtn.Button(self.x+self.colWidth*c,
                                self.y+self.rowHeight*r,
                                self.colWidth,
                                self.rowHeight,
                                textColor2,
                                btnTxt,
                                menuTextSize,
                                bkImg,
                                img)
                value.screenNum = s
                c=0
                r+=1
            # value.surface.fill(gray22)
            self.btnDict[key] = value

    def blitButtons(self):
        for i in range(1,len(self.btnDict)+1):
            btn = self.btnDict[self.btnKey+str(i)]
            if btn.btnTxt is not None:
                btn.renderBtnTxt()
            displaySurface.blit(btn.surface,(btn.x,btn.y))
            if btn.bkImg is not None:
                displaySurface.blit(btn.bkImg,btn.bkImgCent)
            if btn.img is not None:
                displaySurface.blit(btn.img,btn.imgCent)


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
    def drawScreens(self):
        for s in range(0,len(self.screenList)):
            screen = self.screenList[s]
            if screen.isDrawn:
                displaySurface.blit(screen.surface,screen.originPoint)
                if len(screen.screenImgs) > 0:
                    for i in range(0,len(screen.screenImgs)):
                        img = screen.screenImgs[i]
                        xCentered = screen.x+screen.width/2-img.get_width()/2
                        yCentered = screen.y+screen.height/2-img.get_height()/2
                        displaySurface.blit(screen.screenImgs[i],(xCentered,yCentered))
                if len(screen.btnDict) > 0:
                    screen.blitButtons()

def refreshMenuScreens(subScreenList:list[MenuSubScreen]):
    for s in range(0,len(subScreenList)):
        subScreenList[s].surface = pygame.Surface((subScreenList[s].width, subScreenList[s].height), pygame.SRCALPHA)
        if subScreenList[s].bgColor is not None:
            subScreenList[s].surface.fill(subScreenList[s].bgColor)