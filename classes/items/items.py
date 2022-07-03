from enum import Enum
import uuid


class Weight(Enum):
    light = 1
    medium = 2
    heavy = 3


class Item():
    def __init__(self, name, mass: Weight = Weight.medium):
        self.id = uuid.uuid4()
        self.name = name
        self.mass = mass
