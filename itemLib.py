# Standard library imports
import pygame

# Custom class imports
import item

#------------- Weapon Library ---------------#
#                                            #
## Starter Pistol ##
pistol1 = item.Weapon(1,1,True,False)
pistol1.itemName = "Pistol"
pistol1.itemDescription = "A pistol that you start the game with. Good luck."
####################

## Starter Secondary ##
knife1 = item.Weapon(1,2,False,False)
knife1.itemName = "Butter Knife"
knife1.itemDescription = "Your only line of defense when things get too close. Hope it isn't plastic."
#######################

#### Hand Guns ####

###################

## Automatic Guns ##

####################

#                                            #
#--------------------------------------------#


#--------------- Magic Library --------------#
#                                            #
#Destruction Magics#
iceMagic1 = item.DestructionMagic(5,1,2)
iceMagic1.itemName = "Icicle of Murderous Intent"
iceMagic1.itemDescription = "Shoots a spike of ice that homes in on the nearest enemy and exploads on contact dealing its damage in an AOE."
iceMagic1.miniBossSoulPrice = 1
iceMagic1.mobSoulPrice = 50

fireMagic1 = item.DestructionMagic(500,10,1)
fireMagic1.itemName = "Soul Flare"
fireMagic1.itemDescription = "A burning flare erupts from you dealing massive damage to whatever it hits"
fireMagic1.regionBossSoulPrice = 2 
fireMagic1.miniBossSoulPrice = 2 
fireMagic1.requiresManySoulTypes = True
####################

## Restoration Magics ##
healMagic1 = item.RestorationMagic(5,1,2)
healMagic1.itemName = "Basic Heal"
healMagic1.itemDescription = "Knits small wounds back together healing 5HP."
healMagic1.mobSoulPrice = 10
########################

#                                            #
#--------------------------------------------#
