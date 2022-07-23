class Stats():
    def __init__(self, intel, ref, dex, tech, cool, will, lusk, move, body, emp) -> None:
        self._intel = intel
        self._ref = ref
        self._dex = dex
        self._tech = tech
        self._cool = cool
        self._will = will
        self._lusk = lusk
        self._move = move
        self._body = body
        self._emp = emp

    def as_json(self):
        return {
            'intel': self._intel, 
            'ref': self._ref, 
            'dex': self._dex, 
            'tech': self._tech, 
            'cool': self._cool, 
            'will': self._will, 
            'lusk': self._lusk, 
            'move': self._move, 
            'body': self._body, 
            'emp': self._emp,
        } 
        
