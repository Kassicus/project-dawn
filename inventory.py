#Standard library imports
import itemLib

class Inventory():
    """
    A class that deals with anything that needs an inventory. Stores/Players/Bosses
    """
    def __init__(self) -> None:
        self.inventory = {}

    # a function to add an item to a player's inventory
    def addItem(self, item, inventorySlot):
        """
        A method for adding items to an inventory instance

        item: an item object
        inventorySlot: key to the inventory dictionary for stored items
        """
        self.inventory[inventorySlot] = item

class PlayerInventory(Inventory):
    """
    A class specifically for Player Inventory 
    """
    def __init__(self) -> None:
        super().__init__()
        self.key = "slot"

        self.loadout = {}
        self.loadout["slot1"] = itemLib.pistol1
        self.loadout["slot2"] = None
        self.loadout["slot3"] = None
        self.loadout["slot4"] = None
        self.loadout["slot5"] = None

        self.inventory["slot1"] = itemLib.pistol1
        self.inventory["slot2"] = None
        self.inventory["slot3"] = None
        self.inventory["slot4"] = None
        self.inventory["slot5"] = None
        self.inventory["slot6"] = None
        self.inventory["slot7"] = None
        self.inventory["slot8"] = None
        self.inventory["slot9"] = None
        self.inventory["slot10"] = None
        self.inventory["slot11"] = None
        self.inventory["slot12"] = None
        self.inventory["slot13"] = None
        self.inventory["slot14"] = None
        self.inventory["slot15"] = None
        self.inventory["slot16"] = None
        self.inventory["slot17"] = None
        self.inventory["slot18"] = None
        self.inventory["slot19"] = None
        self.inventory["slot20"] = None
        self.inventory["slot21"] = None
        self.inventory["slot22"] = None
        self.inventory["slot23"] = None
        self.inventory["slot24"] = None