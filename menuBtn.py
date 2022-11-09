# Standard library imports
import os
import string
import pygame
import pygame.color

import pygame.freetype as freetype

class Button():
    def __init__(self,x,y,width,height,btnTxtColor,btnTxt:str=None,btnTxtSize:int=8,bkImg:str=None,img:pygame.Surface=None):
        """
        Object for interactable sub elements in UI/Menus
        x: x coordinate for the origin point of the button
        y: y coordinate for the origin point of the button
        width: width of the button
        height: height of the button
        btnTxtColor: color of text that is on the button
        btnTxt: text that will appear on the button
        btnTxtSize: size of text to show on button
        """
        self.font = freetype.Font("data/Orbitron-Regular.ttf")
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width,height),pygame.SRCALPHA)
        self.btnTxt = btnTxt
        self.btnTxtColor = btnTxtColor
        self.btnTxtSize = btnTxtSize
        self.isHovered = False
        self.isActive = False
        self.screenNum = 0
        self.btnTxtRect = self.font.get_rect(btnTxt , size = btnTxtSize)
        self.btnTxtRect.center = self.surface.get_rect().center

        if bkImg is not None:
            self.bkImg = bkImg
            self.bkImgCent = self.setImgCent(bkImg)
        else:
            self.bkImg = None
            self.bkImgCent = None
        if img is not None:
            self.img = img
            self.imgCent = self.setImgCent(img)
        else:
            self.img = None
            self.imgCent = None

    def setImgCent(self,img:pygame.Surface):
        imgXCent = self.x+self.width / 2 - img.get_width() / 2
        imgYCent = self.y+self.height / 2 - img.get_height() / 2 #similarly..
        imgCent = (imgXCent,imgYCent)
        return imgCent
    def renderBtnTxt(self):
        self.font.render_to(
            self.surface,
            self.btnTxtRect,
            self.btnTxt,
            self.btnTxtColor,
            size=self.btnTxtSize,
            style=freetype.STYLE_UNDERLINE
            )
        self.font.pad = False
