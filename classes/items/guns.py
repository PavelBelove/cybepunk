from classes.items.weapon import Weapon


class Ammo():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantyty = quantity


class Guns(Weapon):
    def __init__(self, ammo, gun_range):
        self.ammo = ammo
        self.gun_range = gun_range
