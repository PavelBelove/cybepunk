import uuid


def random_name():
    return f'location-{uuid.uuid4()}'


class Location():
    def __init__(self, name):
        self.name = name if name != None else random_name()


class Party():
    def __init__(self, characters):
        self.characters = characters


class Fight():
    def __init__(self, location, party, enemies_party):
        self.location = location if location != None else Location()
        self.party = party if party != None else Party()
        self.enemies_party = enemies_party if enemies_party != None else Party()
        # TODO: NPC party
        self.characters_order = self.calculate_characters_order(
            self.party, self.enemies_party)

    def calculate_characters_order(self, party, enemies_party):
        initiatives = [(character, character.throw_initiative_dice())
                       for character in (party.characters + enemies_party.characters)]

        def take_initiative(elem):
            return elem[1]

        initiatives.sort(key=take_initiative, reverse=True)

        return initiatives
