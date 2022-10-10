# Standard Library Imports
import pygame

# Generic Base Item Class
# Contains base attributes that all items may have
class Item():
    def __init__(self, itemName, itemDescription):
        self.itemName = itemName
        self.itemDescription = itemDescription
        self.requiresManySoulTypes = False
        self.soulPrice = 0
        
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
    def __init__(self):
        self.damage = 1.5
        self.coolDownTimer = 0
        self.magicCharges = 1

class RestorationMagic(Item):
    def __init__(self):
        self.healAmount = 5
        self.coolDownTimer = 0
        self.magicCharges = 1
        pass
