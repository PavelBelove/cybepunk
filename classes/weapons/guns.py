from classes.weapons.weapon import Weapon


class Ammo(self):
    def __init__(name, price, quantity):
        self.name = name
        self.price = price
        self.quantyty = quantity


class Guns(Weapon):
    def __init__(self, ammo, range):
        self.ammo = ammo
        self.range = range
