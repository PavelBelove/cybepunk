import uuid

knifes_data = {
    'small_knife': {
        'id': uuid.uuid4(),
        'name': 'small_knife',
        'mass': 'light',
        # 'damage': '',
        'hands': 1,
        'price': 10,
        # 'quality': '',
        'is_hidden': True,
        'dices': 2,
        'dice_type': 6,
    },
    'knife': {
        'id': uuid.uuid4(),
        'name': 'knife',
        'mass': 'light',
        # 'damage': '',
        'hands': 1,
        'price': 10,
        # 'quality': '',
        'is_hidden': True,
        'dices': 2,
        'dice_type': 6,
    },
    'machete': {
        'id': uuid.uuid4(),
        'name': 'machete',
        'mass': 'middle',
        # 'damage': '',
        'hands': 1,
        'price': 20,
        # 'quality': '',
        'is_hidden': False,
        'dices': 3,
        'dice_type': 6,
    }
}