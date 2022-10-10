# Standard Library Imports
import pygame

# Generic Base Item Class
# Contains base attributes that all items may have
class Item():
    def __init__(self, itemName, itemDescription):
        self.itemName = itemName
        self.itemDescription = itemDescription
        self.requiresManySoulTypes = False
        self.mobSoulPrice = 0
        self.miniBossSoulPrice = 0
        self.regionBossSoulPrice = 0
        
class OneHandedWeapon(Item):
    def __init__(self, damage, atkSpeed):
        self.isTwoHanded = False
        self.damage = damage
        self.atkSpeed = atkSpeed

class TwoHandedWeapon(Item):
    def __init__(self):
        self.isTwoHanded = True
        self.damage = 2
        self.atkSpeed = 0

class DestructionMagic(Item):
    def __init__(self, damage, coolDownTimer, magicCharges):
        self.damage = damage
        self.coolDownTimer = coolDownTimer
        self.magicCharges = magicCharges

class RestorationMagic(Item):
    def __init__(self, healAmount, coolDownTimer, magicCharges):
        self.healAmount = healAmount
        self.coolDownTimer = coolDownTimer
        self.magicCharges = magicCharges
        pass
